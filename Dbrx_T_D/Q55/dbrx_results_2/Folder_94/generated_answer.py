def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    for i in range(len(circular_list)):
        sub_list = circular_list[i:] + circular_list[:i]
        for j in range(len(sub_list)):
            if sub_list[j:j + 2] == [1, n]:
                result.append(sub_list[j:j + 2])
            elif sub_list[j:j + 3] == [1, 1, n]:
                result.append(sub_list[j:j + 3])
            elif sub_list[j:j + 4] == [1, 1, 1, n]:
                result.append(sub_list[j:j + 4])
            elif sub_list[j:j + 5] == [1, 1, 1, 1, n]:
                result.append(sub_list[j:j + 5])
            else:
                product = 1
                for k in sub_list[j:]:
                    product *= k
                    if product == n:
                        result.append(sub_list[j:])
                    elif product > n:
                        break
    return result