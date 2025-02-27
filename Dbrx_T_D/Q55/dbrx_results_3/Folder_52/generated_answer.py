from itertools import islice, cycle

def lists_with_product_equal_n(l: list[int]) -> list[list[int]]:

    def product_equals_n(sublist: list[int]) -> bool:
        product = 1
        for i in sublist:
            product *= i
            if product > 37:
                return False
            if product == 37:
                return True
        return False
    length = len(l)
    result = []
    for i in range(length):
        for j in range(i, length):
            if product_equals_n(l[i:j + 1]):
                result.append(l[i:j + 1])
    return result