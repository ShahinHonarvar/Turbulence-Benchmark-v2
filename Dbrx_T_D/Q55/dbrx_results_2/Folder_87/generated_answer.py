from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 27
    result = []
    circular_list = list(circular_list)
    if not circular_list:
        return result
    for size in range(1, len(circular_list) + 1):
        for start in range(len(circular_list) - size + 1):
            sub_list = circular_list[start:start + size]
            if sub_list[0] == 0 and len(sub_list) > 1:
                continue
            if all((elem == 0 for elem in sub_list[1:])):
                continue
            if sub_list and all((elem == 1 for elem in sub_list[1:])):
                continue
            if all((elem == n for elem in sub_list)):
                continue
            if all((1 <= elem <= n for elem in sub_list)) and islice(cycle(sub_list), len(sub_list) - 1, None) == sub_list and all((prod == n for prod in [prod for prod in (x * y for x in sub_list for y in sub_list) if prod != 1])):
                result.append(sub_list)
    return result