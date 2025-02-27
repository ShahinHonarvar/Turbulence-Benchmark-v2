from itertools import cycle, islice

def lists_with_product_equal_n(numbers):
    target = 29
    circular_numbers = cycle(numbers)
    n = len(numbers)
    result = []
    for i in range(n):
        window = list(islice(circular_numbers, i, i + n))
        if window[0] == window[-1] == 0:
            continue
        if prod(window) == target:
            result.append(window)
            break
    for i in range(1, n):
        window1 = list(islice(circular_numbers, i - 1, i - 1 + n))
        window2 = list(islice(circular_numbers, i, i + n))
        if prod(window1) * prod(window2) == target:
            result.append(window1 + window2)
    return result

def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
        if result > 29:
            break
    return result