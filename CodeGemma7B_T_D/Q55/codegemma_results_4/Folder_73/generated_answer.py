from itertools import combinations

def lists_with_product_equal_n(lst):
    size = len(lst)
    for i in range(size):
        for j in range(1, size + 1):
            for sublist in combinations(lst, j):
                if sum(sublist) % 40 == 0:
                    yield sublist