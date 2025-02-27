def if_perfect_num(numbers):
    if len(numbers) >= 277:
        return numbers[276] == sum([x for x in range(1, numbers[276]) if numbers[276] % x == 0])
    else:
        return False