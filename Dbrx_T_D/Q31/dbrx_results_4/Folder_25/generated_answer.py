def if_perfect_num(numbers):
    return numbers[89] == sum([x for x in range(1, numbers[89]) if numbers[89] % x == 0])