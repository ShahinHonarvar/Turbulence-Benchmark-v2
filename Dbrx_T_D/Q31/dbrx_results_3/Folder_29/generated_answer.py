def if_perfect_num(numbers):
    if len(numbers) > 19:
        return numbers[19] == sum([x for x in range(1, numbers[19]) if numbers[19] % x == 0])
    else:
        return False