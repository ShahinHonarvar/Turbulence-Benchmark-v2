from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if j == i:
                    yield lst[i:i + 1]
                elif prod(lst[i:j + 1]) == n:
                    yield lst[i:j + 1]

    def prod(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return [sublist for sublist in sublists_with_product_equal_n(lst, 632) if len(sublist) <= len(lst)]