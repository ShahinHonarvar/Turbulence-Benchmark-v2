def if_perfect_num(numbers):
    if len(numbers) > 17:
        return numbers[16] == sum([x for x in range(1, numbers[16]) if numbers[16] % x == 0])
    else:
        return False