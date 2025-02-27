def sum_ints_div_by_either_nums(numbers):
    return sum((numbers[i] for i in range(55, 67) if numbers[i] % 22 == 0 or numbers[i] % 82 == 0))