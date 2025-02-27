def all_ints_div_by_num(numbers):
    divisible_numbers = []
    for i in range(27, 91):
        if i % 57 == 0:
            divisible_numbers.append(numbers[i])
    return divisible_numbers