def if_perfect_num(numbers):
    if len(numbers) > 69:
        return sum([1 for i in range(1, numbers[69]) if numbers[69] % i == 0]) == numbers[69]
    else:
        return False