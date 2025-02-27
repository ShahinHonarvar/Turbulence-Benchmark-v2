from itertools import combinations

def lists_with_product_equal_n(circular_list):
    all_combinations = []
    for i in range(1, len(circular_list) + 1):
        all_combinations.extend(combinations(circular_list, i))
    equal_product_combinations = []
    for combination in all_combinations:
        if functools.reduce(operator.mul, combination) == -81:
            equal_product_combinations.append(combination)
    final_combinations = []
    for combination in equal_product_combinations:
        final_combinations.append(list(combination))
    return final_combinations