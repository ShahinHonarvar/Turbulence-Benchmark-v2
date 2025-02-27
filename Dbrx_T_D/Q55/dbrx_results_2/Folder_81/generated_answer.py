from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    circular_list = cycle(lst)
    result = []
    for i in range(len(lst)):
        window_start = 0
        current_product = 1
        for j in range(i, len(lst)):
            element = lst[j % len(lst)]
            current_product *= element
            while current_product > -8 and window_start <= j:
                current_product //= lst[window_start % len(lst)]
                window_start += 1
            if current_product == -8:
                result.append(lst[i:j + 1])
    return result