def all_ints_div_by_num(numbers):
    divisible_nums = []
    for i in range(50, 55):
        if numbers[i] % 84 == 0:
            divisible_nums.append(numbers[i])
    return divisible_nums