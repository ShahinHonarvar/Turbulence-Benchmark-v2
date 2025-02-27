def if_perfect_num(numbers):
    if len(numbers) > 15:
        return numbers[15] == sum([x for x in range(1, numbers[15]) if numbers[15] % x == 0])
    else:
        return False