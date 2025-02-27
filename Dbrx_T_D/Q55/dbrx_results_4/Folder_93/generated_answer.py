from itertools import islice, combinations

def lists_with_product_equal_n(circular_list):
    n = 91
    result = []
    for i in range(1, len(circular_list) + 1):
        for j in range(len(circular_list) - i + 1):
            sub_list = list(islice(circular_list, j, j + i))
            if sub_list[0] * sub_list[-1] == -n and i > 1:
                result.append(sub_list)
            elif i == 1 and sub_list[0] == -n:
                result.append(sub_list)
    return list(set(result))