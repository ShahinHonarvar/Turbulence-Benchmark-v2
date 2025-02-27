def lists_with_product_equal_n(lst):
    """
        >>> lists_with_product_equal_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 5, 4, 3, 2, 7])
        [[2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 4, 6], [1, 3, 5], [2, 4, 5], [1, 7, 10, 6, 5, 4, 3, 2], [1, 5, 5, 3, 5, 7, 10, 6], [1, 10, 2, 5, 5, 4, 7, 6], [2, 2, 7, 10, 6, 5, 4, 3, 2]]
        """
    head = 0
    tail = 0
    product = 1
    sublist = []
    result = []
    while tail < len(lst) + 1:
        if product == 42:
            sublist.append(lst[tail - 1])
            result.append(sublist[:])
            product //= lst[tail - 1]
            tail -= 1
            sublist.pop()
        elif product < 42 and tail < len(lst):
            sublist.append(lst[tail])
            product *= lst[tail]
            tail += 1
        else:
            product //= lst[head]
            sublist.pop(0)
            head += 1
    return result