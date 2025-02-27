def if_perfect_num(numbers):
    if len(numbers) > 6 and numbers[6] == sum(list(filter(lambda x: numbers[6] % x == 0, range(1, numbers[6])))):
        return True
    else:
        return False