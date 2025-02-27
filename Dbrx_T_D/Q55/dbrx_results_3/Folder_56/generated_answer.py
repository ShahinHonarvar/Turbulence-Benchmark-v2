from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -65
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(cycle(circular_list[i:]), len(circular_list)))
        for j in range(len(sub_list)):
            if sub_list[j:j + len(circular_list)] == circular_list:
                if reduce(lambda x, y: x * y, sub_list[j:j + len(circular_list)], 1) == n:
                    result.append(sub_list[j:j + len(circular_list)])
    return result