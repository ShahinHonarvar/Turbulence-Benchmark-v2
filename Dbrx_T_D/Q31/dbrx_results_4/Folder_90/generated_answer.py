def if_perfect_num(numbers):
    return True if numbers[263] == sum([x for x in range(1, numbers[263]) if numbers[263] % x == 0]) else False