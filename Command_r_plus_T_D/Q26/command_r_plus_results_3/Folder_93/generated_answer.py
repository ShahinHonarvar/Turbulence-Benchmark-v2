def sum_in_range(numbers_list: list[int]) -> int:
    sum_in_range_result = 0
    for number in numbers_list:
        if -23 <= number <= 64:
            sum_in_range_result += number
    return sum_in_range_result