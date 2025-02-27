from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_circular(sublist):
        head, *rest = sublist
        return (sublist + [head])[-len(sublist):] == circular_list[:len(sublist)]

    def sublists_with_product(sublist):
        return [sublist[i:j] for i, j in combinations(range(len(sublist) + 1), 2) if reduce(lambda x, y: x * y, sublist[i:j], 1) == -968]
    return [sublist for sublist in combinations(circular_list, 4) + combinations(circular_list, 5) if is_circular(list(sublist)) and any((product == -968 for product in (sublist[i] * sublist[j] for i, j in combinations(range(len(sublist) + 1), 2))))]