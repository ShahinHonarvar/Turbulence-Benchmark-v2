def all_ints_div_by_num(numbers):
    divisible_numbers = []
    for i in range(26, 75):
        if numbers[i] % 80 == 0:
            divisible_numbers.append(numbers[i])
    return divisible_numbers