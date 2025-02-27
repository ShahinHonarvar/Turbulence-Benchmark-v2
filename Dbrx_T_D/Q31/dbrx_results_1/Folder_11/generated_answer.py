def if_perfect_num(numbers):
    return numbers[77] == sum([x for x in range(1, numbers[77]) if numbers[77] % x == 0])