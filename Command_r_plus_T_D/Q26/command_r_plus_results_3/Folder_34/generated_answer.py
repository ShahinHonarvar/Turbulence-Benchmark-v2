def sum_in_range(numbers_list: list[int]) -> int:
    sum_ = 0
    for num in numbers_list:
        if 4 <= num <= 7:
            sum_ += num
    return sum_