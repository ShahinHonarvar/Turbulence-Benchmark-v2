def if_perfect_num(numbers):
    if len(numbers) > 926:
        return numbers[925] == sum([x for x in range(1, numbers[925]) if numbers[925] % x == 0])
    return False