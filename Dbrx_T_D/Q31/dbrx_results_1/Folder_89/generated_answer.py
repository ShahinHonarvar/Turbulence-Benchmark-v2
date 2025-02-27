def if_perfect_num(numbers):
    if len(numbers) > 18:
        return numbers[18] == sum([i for i in range(1, numbers[18]) if numbers[18] % i == 0])
    else:
        return False