def if_perfect_num(numbers):
    if len(numbers) > 99 and numbers[99] > 0 and (sum([x for x in range(1, numbers[99]) if numbers[99] % x == 0]) == numbers[99]):
        return True
    else:
        return False