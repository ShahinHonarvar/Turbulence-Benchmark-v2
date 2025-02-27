def if_perfect_num(numbers):
    if len(numbers) > 312:
        return numbers[311] == sum([i for i in range(1, numbers[311]) if numbers[311] % i == 0])
    else:
        return False