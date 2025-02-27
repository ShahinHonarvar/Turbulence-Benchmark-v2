def if_perfect_num(numbers):
    if len(numbers) > 91:
        return numbers[90] == sum([i for i in range(1, numbers[90]) if numbers[90] % i == 0])
    else:
        return False