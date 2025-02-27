from itertools import combinations, islice

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        for sub_numbers in combinations(numbers, i):
            circular_sub_numbers = sub_numbers + (sub_numbers[0],)
            if sub_numbers != circular_sub_numbers:
                continue
            product = 1
            for num in circular_sub_numbers:
                product *= num
                if product == -46:
                    result.append(circular_sub_numbers)
                    break
                elif product > -46:
                    break
    return result