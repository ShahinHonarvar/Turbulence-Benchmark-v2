def if_perfect_num(numbers):
    if len(numbers) > 93:
        return numbers[93] == sum([i for i in range(1, numbers[93]) if numbers[93] % i == 0])
    else:
        return False