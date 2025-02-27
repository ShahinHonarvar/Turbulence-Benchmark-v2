from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-46):
    result = []
    for i in range(len(numbers)):
        sublist = list(islice(cycle(numbers[i:]), len(numbers)))
        if product(sublist) == target:
            result.append(sublist)
    return result

def product(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)