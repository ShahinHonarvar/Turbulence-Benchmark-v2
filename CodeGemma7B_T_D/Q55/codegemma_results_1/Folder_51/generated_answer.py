def lists_with_product_equal_n(circ):
    n = -44
    lists = []
    current_list = []
    current_product = 1
    current_index = 0
    for idx, num in enumerate(circ):
        current_product *= num
        while current_product == n:
            lists.append(current_list[:])
            current_index += 1
        while current_product > n:
            current_product //= circ[current_index]
            current_index += 1
        current_list.append(num)
    return lists