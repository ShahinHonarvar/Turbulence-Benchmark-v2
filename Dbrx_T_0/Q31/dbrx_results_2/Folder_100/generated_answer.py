def if_perfect_num(numbers):
    if len(numbers) > 99 and numbers[99] == sum([i for i in range(1, numbers[99]) if numbers[99] % i == 0]):
        return True
    else:
        return False