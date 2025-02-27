from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        window = list(islice(cycle(numbers[i:]), len(numbers)))
        for j in range(len(window)):
            if window[j] == -16:
                result.append(window[:j + 1])
            elif window[j] != 0:
                window[j + 1] *= window[j]
    return result