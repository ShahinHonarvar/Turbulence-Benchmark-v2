def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for number in numbers_list:
        if 368 <= number <= 679:
            sum_result += number
    return sum_result