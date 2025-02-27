from itertools import combinations

def lists_with_product_equal_n(lst):
    n = 46
    n_factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            n_factors.extend([i, n // i])
    n_factors = list(set(n_factors))

    def check_product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product == n

    def circular_sublists(lst):
        for i in range(len(lst)):
            for j in range(i + 1, i + len(lst)):
                sublist = lst[i:j % len(lst)]
                if all((num in n_factors for num in sublist)):
                    yield sublist
    result = []
    for sublist in circular_sublists(lst):
        if check_product(sublist):
            result.append(sublist)
    return result