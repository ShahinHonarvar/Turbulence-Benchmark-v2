def if_perfect_num(numbers):
    return sum([i for i in numbers[:96] if numbers[96] % i == 0]) == numbers[96]