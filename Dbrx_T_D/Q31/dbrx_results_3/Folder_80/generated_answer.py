def if_perfect_num(numbers):
    return True if numbers[746] == sum([x for x in range(1, numbers[746]) if numbers[746] % x == 0]) else False