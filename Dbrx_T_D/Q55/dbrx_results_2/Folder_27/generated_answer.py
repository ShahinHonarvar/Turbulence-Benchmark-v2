from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-82):
    sublists = []
    for i in range(len(numbers)):
        window_sublists = []
        for j in range(1, len(numbers) - i + 1):
            window = list(islice(cycle(numbers[i:i + j]), len(numbers)))
            if len(window) == 1 and window[0] == target:
                window_sublists.append(window)
                break
            elif len(window) > 1 and reduce(lambda x, y: x * y, window) == target:
                window_sublists.append(window)
            elif len(window) > 1 and reduce(lambda x, y: x * y, window) == target:
                window_sublists.append(window)
        sublists.extend(window_sublists)
    return sublists