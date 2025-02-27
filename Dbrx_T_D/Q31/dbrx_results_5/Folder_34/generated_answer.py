def if_perfect_num(numbers):
    if len(numbers) > 97:
        return numbers[96] == sum([x for x in range(1, numbers[96]) if numbers[96] % x == 0])
    else:
        return False