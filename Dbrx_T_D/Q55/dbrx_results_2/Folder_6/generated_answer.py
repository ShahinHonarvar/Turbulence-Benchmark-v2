from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    for i in range(1, len(circular_list) + 1):
        for combo in combinations(circular_list, i):
            if n == 1:
                result.append(list(combo))
            elif n % combo[0] == 0:
                new_combo = [n // combo[0]] + list(combo)
                result.append(new_combo)
            elif n % combo[-1] == 0:
                new_combo = list(combo) + [n // combo[-1]]
                result.append(new_combo)
    return [sublist for sublist in result if sublist == tuple(sorted(sublist)) and circular_list.index(sublist[0]) == circular_list.index(sublist[-1]) or circular_list.index(sublist[0]) == (circular_list.index(sublist[-1]) - 1) % len(circular_list)]