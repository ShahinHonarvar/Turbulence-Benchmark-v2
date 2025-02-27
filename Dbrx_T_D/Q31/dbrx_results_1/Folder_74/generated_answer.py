def if_perfect_num(numbers):
    if len(numbers) > 48 and numbers[48] == sum([x for x in range(1, numbers[48]) if numbers[48] % x == 0]):
        return True
    else:
        return False