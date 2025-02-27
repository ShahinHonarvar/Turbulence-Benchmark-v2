def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    if n == 0:
        return result
    for i in range(n):
        current_product = 1
        for j in range(n):
            index = (i + j) % n
            current_product *= circular_list[index]
            if current_product == 27:
                sublist_start = i
                sublist_end = index + 1 if index + 1 <= n else index + 1 - n
                if sublist_start < sublist_end:
                    result.append(circular_list[sublist_start:sublist_end])
                else:
                    result.append(circular_list[sublist_start:] + circular_list[:sublist_end])
            if current_product == 0:
                break
    return result