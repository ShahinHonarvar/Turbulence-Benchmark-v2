def composite_nums_between_indices(L):
    return {l for l in L[2:3] if sum((factor ** 2 for factor in range(3, int(l ** 0.5) + 1, 2))) > l}