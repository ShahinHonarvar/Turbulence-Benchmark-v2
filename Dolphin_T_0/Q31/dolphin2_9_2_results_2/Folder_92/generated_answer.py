def if_perfect_num(numbers):
    if numbers[0] == 0:
        return False
    else:
        return sum(list(filter(lambda x: numbers[0] % x == 0, range(1, numbers[0] + 1)))) == numbers[0]