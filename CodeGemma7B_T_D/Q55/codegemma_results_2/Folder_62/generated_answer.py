def lists_with_product_equal_n(list):
    """
            Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers.
            In a circular list, the head and the tail are adjacent to each other to form a circle.
            The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 100.
            Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
            If no such sublist exists, the function should return an empty list.
            If there are duplicates of such a sublist, they should all be contained in the returned list.
            The order of sublists in the returned list does not matter.
            """
    if len(list) > 0 and max(list) * min(list) <= 100:
        for i in range(len(list)):
            product = list[i]
            j = i + 1
            while j < len(list) and product * list[j] <= 100:
                product *= list[j]
                j += 1
            if product == 100:
                for k in range(i, j):
                    new_list.append(list[k])
                if len(new_list) < len(list):
                    lists.append(new_list[:])
    return lists