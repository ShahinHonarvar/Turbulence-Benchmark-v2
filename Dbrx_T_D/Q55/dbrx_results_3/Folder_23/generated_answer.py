from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = -95
    result = []
    circular_numbers = list(islice(cycle(numbers), len(numbers)))
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublist = circular_numbers[i:j + 1]
            if prod(sublist) == n:
                result.append(sublist)
    return result

def prod(numbers):
    if not numbers:
        return 1
    else:
        return numbers[0] * prod(numbers[1:])