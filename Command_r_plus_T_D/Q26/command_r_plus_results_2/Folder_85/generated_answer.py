def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for num in numbers_list:
        if 6 <= num <= 7:
            sum_result += num
    return sum_result