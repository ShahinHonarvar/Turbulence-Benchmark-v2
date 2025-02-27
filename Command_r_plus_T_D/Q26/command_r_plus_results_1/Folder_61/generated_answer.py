def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for num in numbers_list:
        if 8 <= num <= 9:
            sum_result += num
    return sum_result