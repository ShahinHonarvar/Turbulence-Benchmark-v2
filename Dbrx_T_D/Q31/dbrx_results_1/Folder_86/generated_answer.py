def if_perfect_num(numbers):
    if 194 < len(numbers) and sum((x for x in range(1, numbers[194]) if numbers[194] % x == 0)) == numbers[194]:
        return True
    else:
        return False