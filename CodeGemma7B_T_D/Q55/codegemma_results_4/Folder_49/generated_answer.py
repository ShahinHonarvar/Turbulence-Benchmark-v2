def lists_with_product_equal_n(lst):
    """
    Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers. In a circular list, the head and the tail are adjacent to each other to form a circle. The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -61. Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """
    checked = set()
    answer = []
    for i in range(len(lst)):
        current_lst = [lst[i]]
        current_product = lst[i]
        for j in range(i + 1, len(lst)):
            current_lst.append(lst[j])
            current_product *= lst[j]
            if current_product == -61 and tuple(current_lst) not in checked:
                answer.append(current_lst[:])
                checked.add(tuple(current_lst))
            if current_product > -61:
                break
    return answer