from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-938):
    result = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublist = list(islice(cycle(numbers[i:j + 1]), len(numbers)))
            if len(sublist) <= len(numbers) and all((num != 0 for num in sublist)) and all((isinstance(num, int) for num in sublist)) and (product(sublist) == target):
                result.append(sublist)
    return result

def product(numbers):
    p = 1
    for num in numbers:
        p *= num
    return p