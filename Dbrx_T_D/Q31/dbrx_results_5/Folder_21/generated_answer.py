def if_perfect_num(numbers):
    if len(numbers) > 410 and numbers[410] == sum([x for x in range(1, numbers[410]) if numbers[410] % x == 0]):
        return True
    else:
        return False