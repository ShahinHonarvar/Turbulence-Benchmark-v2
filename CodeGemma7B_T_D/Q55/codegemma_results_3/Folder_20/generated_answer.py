from itertools import permutations

def lists_with_product_equal_n(lst, n):
    permutations_lst = list(permutations(lst))
    filtered_lst = []
    for perm in permutations_lst:
        for i in range(len(perm)):
            product = 1
            sublst = []
            for j in range(i, len(perm)):
                product *= perm[j]
                sublst.append(perm[j])
                if product == n:
                    filtered_lst.append(sublst)
    return filtered_lst