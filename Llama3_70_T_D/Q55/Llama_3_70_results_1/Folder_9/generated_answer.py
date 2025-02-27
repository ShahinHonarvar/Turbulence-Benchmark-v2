import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for size in range(1, n + 1):
        for i in range(n):
            for sublst in itertools.islice(itertools.cycle(lst), i, i + size):
                if sublst[0] * sublst[1] == -36 and len(sublst) == 2:
                    result.add(tuple(sublst))
                elif len(sublst) > 2 and sum(sublst) == -36 and (len(sublst) == 3):
                    result.add(tuple(sublst))
                elif len(sublst) > 3:
                    product = 1
                    for item in sublst:
                        product *= item
                        if product == -36:
                            result.add(tuple(sublst))
    return [list(item) for item in result]