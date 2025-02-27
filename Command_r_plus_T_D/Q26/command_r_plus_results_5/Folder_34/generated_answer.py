def sum_in_range(numbers_list: list[int]) -> int:
    total_sum = 0
    for number in numbers_list:
        if 4 <= number <= 7:
            total_sum += number
    return total_sum