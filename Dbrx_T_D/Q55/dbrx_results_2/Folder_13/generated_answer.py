from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = 54
    result = []
    for i in range(len(numbers)):
        window = list(islice(cycle(numbers[i:i + len(numbers)]), 0, n))
        if len(window) < n:
            break
        if prod(window) == n:
            result.append(window)
    return result

def prod(numbers):
    p = 1
    for num in numbers:
        p *= num
    return p