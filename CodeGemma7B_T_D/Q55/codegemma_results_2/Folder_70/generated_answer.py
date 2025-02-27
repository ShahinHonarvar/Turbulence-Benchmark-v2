from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        circular_list.append(circular_list.pop(0))
        nums = set(circular_list)
        for j in range(1, len(nums) + 1):
            for combo in combinations(nums, j):
                if combo and combo[0] != 0 and (combo[-1] != 0) and (combo[0] == combo[-1]):
                    product = 1
                    for num in combo:
                        product *= num
                    if product == 32:
                        sublists.append(combo)
    return sublists