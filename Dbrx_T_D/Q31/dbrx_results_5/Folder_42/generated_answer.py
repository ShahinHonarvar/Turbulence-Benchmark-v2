def if_perfect_num(numbers):
    if len(numbers) >= 277:
        return numbers[276] == sum([i for i in range(1, numbers[276]) if numbers[276] % i == 0])
    else:
        return False