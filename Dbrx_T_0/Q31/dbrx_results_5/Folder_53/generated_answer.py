def if_perfect_num(numbers):
    if len(numbers) > 73:
        return numbers[72] == sum([x for x in range(1, numbers[72]) if numbers[72] % x == 0])
    else:
        return False