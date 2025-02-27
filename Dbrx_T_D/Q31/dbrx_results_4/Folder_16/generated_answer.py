def if_perfect_num(numbers):
    return True if numbers[162] == sum([x for x in range(1, numbers[162]) if numbers[162] % x == 0]) else False