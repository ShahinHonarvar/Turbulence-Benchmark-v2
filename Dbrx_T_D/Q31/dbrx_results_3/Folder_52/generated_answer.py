def if_perfect_num(numbers):
    return numbers[477] == sum([x for x in range(1, numbers[477]) if numbers[477] % x == 0])