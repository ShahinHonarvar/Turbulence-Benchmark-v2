def if_perfect_num(numbers):
    return numbers[537] == sum([x for x in range(1, numbers[537]) if numbers[537] % x == 0])