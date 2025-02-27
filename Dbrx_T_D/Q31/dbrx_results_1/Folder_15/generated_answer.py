def if_perfect_num(numbers):
    if len(numbers) > 10:
        return numbers[10] == sum([x for x in range(1, numbers[10]) if numbers[10] % x == 0])
    else:
        return False