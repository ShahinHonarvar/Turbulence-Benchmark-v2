def if_perfect_num(numbers):
    return numbers[684] == sum([x for x in range(1, numbers[684]) if numbers[684] % x == 0])