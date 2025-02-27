def all_ints_div_by_num(numbers):
    divisible_by_3 = []
    for i in range(4, 5):
        if numbers[i] % 3 == 0:
            divisible_by_3.append(numbers[i])
    return divisible_by_3