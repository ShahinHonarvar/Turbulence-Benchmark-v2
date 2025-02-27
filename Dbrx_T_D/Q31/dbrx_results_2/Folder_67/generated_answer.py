def if_perfect_num(numbers):
    if len(numbers) > 43:
        perfect_number = sum([i for i in range(1, numbers[43]) if numbers[43] % i == 0])
        return numbers[43] == perfect_number
    else:
        return False