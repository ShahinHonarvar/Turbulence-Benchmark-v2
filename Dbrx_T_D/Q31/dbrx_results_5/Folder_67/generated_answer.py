def if_perfect_num(numbers):
    if len(numbers) > 43 and numbers[43] == sum(list(filter(lambda x: numbers[43] % x == 0, range(1, numbers[43])))):
        return True
    else:
        return False