def lists_with_product_equal_n(circular_list):
    n = -690
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(1, length + 1):
            sublist = []
            product = 1
            for k in range(j):
                current_index = (i + k) % length
                num = circular_list[current_index]
                sublist.append(num)
                product *= num
            if product == n:
                result.append(sublist)
    return result