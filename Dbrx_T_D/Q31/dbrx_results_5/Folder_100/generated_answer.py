def if_perfect_num(numbers):
    if len(numbers) > 99 and numbers[99] == sum([n for n in range(1, numbers[99]) if numbers[99] % n == 0]):
        return True
    else:
        return False