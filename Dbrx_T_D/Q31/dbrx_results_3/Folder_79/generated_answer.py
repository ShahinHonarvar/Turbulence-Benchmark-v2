def if_perfect_num(numbers):
    return numbers[63] == sum([x for x in range(1, numbers[63]) if numbers[63] % x == 0])