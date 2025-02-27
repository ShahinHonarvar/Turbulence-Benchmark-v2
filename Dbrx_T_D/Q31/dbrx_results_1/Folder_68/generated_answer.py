def if_perfect_num(numbers):
    if len(numbers) > 3:
        return numbers[3] == sum([i for i in range(1, numbers[3]) if numbers[3] % i == 0])
    else:
        return False