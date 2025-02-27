def if_perfect_num(numbers):
    if len(numbers) > 34:
        return numbers[33] == sum([x for x in range(1, numbers[33]) if numbers[33] % x == 0])
    else:
        return False