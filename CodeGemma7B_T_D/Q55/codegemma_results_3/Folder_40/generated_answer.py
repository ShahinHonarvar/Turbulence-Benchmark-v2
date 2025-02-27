def lists_with_product_equal_n(circular_list):
    """
            This function takes an argument, a circular list of integers.
            In a circular list, the head and the tail are adjacent to each other to form a circle.
            The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -9.
            Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
            If no such sublist exists, the function should return an empty list.
            If there are duplicates of such a sublist, they should all be contained in the returned list.
            The order of sublists in the returned list does not matter.
            """
    selected = set()
    results = []

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def find_sublist_product_helper(index):
        nonlocal selected
        nonlocal circular_list
        nonlocal results
        if index == len(circular_list):
            if product(circular_list) == -9 and len(selected) > 0:
                results.append(list(selected))
            return
        circular_list[index], circular_list[0] = (circular_list[0], circular_list[index])
        for i in range(index + 1):
            if i not in selected:
                selected.add(i)
                find_sublist_product_helper(i + 1)
                selected.remove(i)
        circular_list[index], circular_list[0] = (circular_list[0], circular_list[index])
    find_sublist_product_helper(0)
    return results