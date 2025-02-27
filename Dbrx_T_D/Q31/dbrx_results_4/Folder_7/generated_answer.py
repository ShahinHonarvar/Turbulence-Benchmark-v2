def if_perfect_num(numbers):
    return numbers[851] == sum([x for x in range(1, numbers[1]) if numbers[1] % x == 0])