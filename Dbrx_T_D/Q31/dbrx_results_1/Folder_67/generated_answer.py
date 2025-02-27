def if_perfect_num(numbers):
    if len(numbers) > 43 and numbers[43] == sum([x for x in range(1, numbers[43]) if numbers[43] % x == 0]):
        return True
    else:
        return False