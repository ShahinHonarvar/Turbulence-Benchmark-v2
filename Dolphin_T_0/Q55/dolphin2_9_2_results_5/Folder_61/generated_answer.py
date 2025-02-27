from sympy import nextprime

def find_product_equal_n(lst):
    prime_numbers = [nextprime(x) for x in lst if x != 0]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] in prime_numbers:
                yield [lst[i], lst[j]]

def lists_with_product_equal_n(lst):
    result = []
    for p in find_product_equal_n(lst):
        for l in range(len(p)):
            for r in range(l + 1, len(p) + 1):
                if p[l:r] not in result:
                    result.append(p[l:r])
    return result