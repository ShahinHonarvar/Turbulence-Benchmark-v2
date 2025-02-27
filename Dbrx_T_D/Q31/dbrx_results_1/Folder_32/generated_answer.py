def if_perfect_num(numbers):
    return numbers[849] == sum([x for x in range(1, numbers[849]) if numbers[849] % x == 0])