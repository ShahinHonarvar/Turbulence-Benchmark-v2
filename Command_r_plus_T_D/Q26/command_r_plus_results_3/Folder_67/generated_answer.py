def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for number in numbers_list:
        if 31 <= number <= 50:
            sum_result += number
    return sum_result