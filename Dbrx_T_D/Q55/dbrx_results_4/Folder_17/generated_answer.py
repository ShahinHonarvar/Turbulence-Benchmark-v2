from itertools import islice, cycle, combinations

def lists_with_product_equal_n(numbers):
    result = []
    for sublength in range(1, len(numbers) + 1):
        for combination in combinations(numbers, sublength):
            if sublength < len(numbers):
                circular_combination = islice(cycle(list(combination)), sublength - 1, len(numbers) - 1)
            else:
                circular_combination = list(combination)
            if len(circular_combination) > 1 and all((x > 0 for x in circular_combination)):
                product = 1
                for num in circular_combination:
                    product *= num
                if product == 18:
                    result.append(list(circular_combination))
                    break
    return result