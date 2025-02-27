def if_perfect_num(numbers):
    if len(numbers) > 72:
        return numbers[71] == sum([x for x in range(1, numbers[71]) if numbers[71] % x == 0])
    else:
        return False