def sum_in_range(numbers_list: list[int]) -> int:
    sum_in_range_result = 0
    for number in numbers_list:
        if 73 <= number <= 84:
            sum_in_range_result += number
    return sum_in_range_result