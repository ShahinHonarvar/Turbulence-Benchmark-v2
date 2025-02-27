def if_perfect_num(numbers):
    return numbers[985] == sum([x for x in range(1, numbers[985]) if numbers[985] % x == 0])