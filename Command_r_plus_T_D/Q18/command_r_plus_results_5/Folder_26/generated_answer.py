def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(69, 71):
        if index < len(numbers_list):
            num = numbers_list[index]
            if num % 72 == 0 or num % 70 == 0:
                total_sum += num
    return total_sum