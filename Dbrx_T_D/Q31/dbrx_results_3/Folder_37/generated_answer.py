def if_perfect_num(numbers):
    if len(numbers) > 28:
        return numbers[27] == sum([i for i in range(1, numbers[27]) if numbers[27] % i == 0])
    else:
        return False