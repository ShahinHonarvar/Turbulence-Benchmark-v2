def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for num in numbers_list:
        if 86 <= num <= 90:
            sum_result += num
    return sum_result