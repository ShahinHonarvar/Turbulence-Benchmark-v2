from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -8
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(cycled(i), i))
        if sub_list:
            if n in (sub_list[0] * sub_list[-1], *map(lambda x: n // x, sub_list)):
                result.append(sub_list)
    return result

def cycled(start):
    circular_list = list(start)
    while True:
        for i in range(len(circular_list)):
            yield circular_list[i]
        circular_list.append(circular_list.pop(0))