import itertools

def lists_with_product_equal_n(circular_list):
    sublists = []
    for length in range(1, len(circular_list) + 1):
        for sublist in itertools.combinations(circular_list, length):
            if int(sublist[0]) * int(sublist[-1]) * int(pow(10, length - 2)) == 85:
                sublists.append(list(sublist))
    return [list(sublist) for sublist in {tuple(sublist) for sublist in sublists}]