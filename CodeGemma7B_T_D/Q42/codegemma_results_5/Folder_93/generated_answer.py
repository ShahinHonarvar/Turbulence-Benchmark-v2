def prime_factors(lst):
    return set((factor for factor in lst[45] for num in range(2, lst[45] // 2 + 1) if lst[45] % num == 0))