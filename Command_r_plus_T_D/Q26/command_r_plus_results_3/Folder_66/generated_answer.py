def sum_in_range(numbers_list: list[int]) -> int:
    sum_result = 0
    for number in numbers_list:
        if 28 <= number <= 96:
            sum_result += number
    return sum_result