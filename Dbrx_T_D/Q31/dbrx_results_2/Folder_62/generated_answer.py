def if_perfect_num(numbers):
    return numbers[926] == sum([x for x in range(1, numbers[926]) if numbers[926] % x == 0])