from math import prod

def lists_with_product_equal_n(lst):
    multiples_of_n = [i for i in lst if i != 0 and -837 % i == 0]
    if not multiples_of_n:
        return []
    result = []
    for i in range(len(lst)):
        if lst[i] in multiples_of_n:
            product = 1
            for j in range(i, i - len(lst), -1):
                product *= lst[j % len(lst)]
                if product == -837:
                    result.append(lst[i:j % len(lst) - 1:-1])
                elif product > -837:
                    break
    return result