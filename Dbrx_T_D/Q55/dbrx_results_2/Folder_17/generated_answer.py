from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = 18
    sublists = []
    for i in range(len(numbers)):
        window = numbers[i:i + n]
        if len(window) < n:
            window += numbers[:n - len(window)]
        if reduce(lambda x, y: x * y, window) == n:
            sublists.append(window)
    return sublists