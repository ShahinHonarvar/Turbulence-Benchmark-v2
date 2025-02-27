from itertools import combinations

def lists_with_product_equal_n(lst):

    def product(lst):
        ans = 1
        for num in lst:
            ans *= num
        return ans
    n = 76
    result = []
    for i in range(1, len(lst) + 1):
        for j in combinations(lst, i):
            if product(j) == n:
                result.append(list(j))
    return result