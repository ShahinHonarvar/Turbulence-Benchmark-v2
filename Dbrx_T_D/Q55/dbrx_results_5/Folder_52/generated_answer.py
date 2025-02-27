from itertools import islice, cycle

def circular_slice(iterable, start, stop):
    it = iter(iterable)
    return list(islice(cycle(it), start, stop))

def lists_with_product_equal_n(lst, n=37):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub = circular_slice(lst, i, j + 1)
            if sub and sub[-1] != 0 and (j - i + 1 <= len(lst)) and all((val != 0 for val in sub)) and all((isinstance(val, int) for val in sub)) and all((val not in (True, False) for val in sub)) and (sub not in result):
                prod = 1
                for k in sub:
                    prod *= k
                if prod == n:
                    result.append(sub)
    return result