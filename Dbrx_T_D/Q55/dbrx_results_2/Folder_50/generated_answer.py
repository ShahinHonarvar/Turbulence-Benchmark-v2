from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(circular_list, i, len(circular_list) - 1)) + list(islice(circular_list, 0, i))
        if sub_list != circular_list and sub_list not in result:
            if sub_list and eval('*'.join(map(str, sub_list))) == n:
                result.append(sub_list)
    return result