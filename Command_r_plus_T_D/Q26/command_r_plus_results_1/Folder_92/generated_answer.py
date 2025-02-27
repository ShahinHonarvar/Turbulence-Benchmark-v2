def sum_in_range(numbers_list: list[int]) -> int:
    sum_ = 0
    for num in numbers_list:
        if 5 <= num <= 9:
            sum_ += num
    return sum_