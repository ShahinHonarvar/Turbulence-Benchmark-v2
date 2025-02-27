from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=10):
    sublists = []
    circular_numbers = cycle(numbers)
    for i in range(len(numbers)):
        sublist = []
        current_product = 1
        for j in range(i, len(numbers)):
            current_number = next(circular_numbers)
            sublist.append(current_number)
            current_product *= current_number
            if current_product == n:
                sublists.append(sublist)
                break
            elif current_product > n:
                break
        circular_numbers = cycle(numbers)
    return sublists