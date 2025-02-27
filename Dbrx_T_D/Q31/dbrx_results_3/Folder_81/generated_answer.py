def if_perfect_num(numbers):
    if len(numbers) > 20:
        return numbers[20] == sum([x for x in range(1, numbers[20]) if numbers[20] % x == 0])
    else:
        return False