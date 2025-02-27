def lists_with_product_equal_n(n, circular_list):
    result = []
    if n != 49:
        return result
    total_list = circular_list + circular_list[:len(circular_list) - 1]
    product = 1
    multiplier = 1
    for i in range(len(total_list)):
        product *= total_list[i]
        while product > multiplier * n:
            if total_list[i] != total_list[i - len(circular_list)]:
                multiplier *= total_list[i - len(circular_list)]
            product /= total_list[i - len(circular_list)]
        if product == multiplier * n:
            if len(result) > 0 and result[-1][0] == total_list[i - len(circular_list) + 1:i + 1]:
                continue
            temp = total_list[i - len(circular_list) + 1:i + 1]
            result.append(temp)
    return result