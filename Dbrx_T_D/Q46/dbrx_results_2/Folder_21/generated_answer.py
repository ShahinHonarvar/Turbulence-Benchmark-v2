import math

def gcf_three_nums(numbers):
    numbers_to_consider = [numbers[412], numbers[932], numbers[337]]
    factor = 1
    for i in range(2, min(numbers_to_consider) + 1):
        if all((num % i == 0 for num in numbers_to_consider)):
            factor = i
    return factor