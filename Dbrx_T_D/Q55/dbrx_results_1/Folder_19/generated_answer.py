from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = -54
    circular_numbers = cycle(numbers)
    result = []
    for i in range(len(numbers)):
        sublist_product = 1
        sublist = []
        current_number = next(circular_numbers)
        for j in range(i, len(numbers)):
            if current_number == 0 and n == 0:
                sublist.append(current_number)
                sublist_product *= current_number
                break
            sublist.append(current_number)
            sublist_product *= current_number
            current_number = next(circular_numbers)
            if sublist_product == n:
                result.append(sublist)
                sublist = []
                sublist_product = 1
                circular_numbers = islice(cycle(numbers), i, None)
    return result