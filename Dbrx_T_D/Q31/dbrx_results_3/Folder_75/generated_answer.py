def if_perfect_num(numbers):
    if len(numbers) > 80 and numbers[80] > 0:
        perfect_number = sum([i for i in range(1, numbers[80]) if numbers[80] % i == 0])
        return numbers[80] == perfect_number
    else:
        return False