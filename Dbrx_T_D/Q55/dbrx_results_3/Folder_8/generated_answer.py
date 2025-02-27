from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=-41):
    results = []
    for i in range(len(numbers)):
        sublist = list(islice(cycle(numbers), i, i + len(numbers)))
        if n == 1:
            results.append([])
        elif n == 0:
            continue
        elif len(sublist) > 1 and any((x != 0 and (not isinstance(x, float)) or x == 1 for x in sublist)):
            product = 1
            for j in sublist:
                product *= j
                if product == n:
                    results.append(sublist)
                elif product < n or product > 0:
                    break
    return results