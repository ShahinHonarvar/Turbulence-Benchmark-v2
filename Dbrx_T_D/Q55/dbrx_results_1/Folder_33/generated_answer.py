def lists_with_product_equal_n(circular_list):
    result = []
    n = -115
    for i in range(len(circular_list)):
        sublists = []
        for j in range(i, len(circular_list)):
            sublists.append(circular_list[j])
            product = 1
            for k in sublists:
                product *= k
            if product == n:
                result.append(sublists[:])
                sublists.pop()
                while sublists and sublists[-1] == circular_list[(j + 1) % len(circular_list)]:
                    sublists.pop()
                j += 1
        sublists.pop()
    return result