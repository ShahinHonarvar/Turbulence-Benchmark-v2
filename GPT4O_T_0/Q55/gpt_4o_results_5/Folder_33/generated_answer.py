def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == -115:
                sublist = []
                for i in range(start, end + 1):
                    sublist.append(circular_list[i % n])
                result.append(sublist)
            if product == 0:
                break
    return result