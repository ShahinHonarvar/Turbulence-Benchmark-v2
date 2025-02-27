from itertools import groupby

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublist = numbers[i:j + 1]
            if prod(sublist) == 6:
                result.append(sublist)

    def by_first_item(pair):
        return pair[0]
    result = [list(g) for k, g in groupby(sorted([(len(q), q) for q in result]), by_first_item)]
    return [x[1] for x in result]

def prod(numbers):
    return reduce(lambda a, b: a * b, numbers, 1)