def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index in range(42, 44):
        if index < len(numbers_list) and (numbers_list[index] % 15 == 0 or numbers_list[index] % 87 == 0):
            sum_divisible += numbers_list[index]
    return sum_divisible