def lists_with_product_equal_n(circular_list):
    n = 27
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % length
                current_num = circular_list[index]
                sublist.append(current_num)
                product *= current_num
                if product == n:
                    result.append(sublist.copy())
                    break
                elif product > n:
                    break
    return result