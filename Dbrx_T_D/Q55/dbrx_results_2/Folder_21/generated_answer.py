from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 851
    result = []
    for i in range(len(circular_list)):
        sub_n = 1
        sub_list = []
        for j in range(i, len(circular_list)):
            sub_n *= circular_list[j]
            sub_list.append(circular_list[j])
            if sub_n == n:
                result.append(sub_list)
            elif sub_n > n:
                break
    return [list(x) for _, x in groupby(sorted(result, key=len), len)]