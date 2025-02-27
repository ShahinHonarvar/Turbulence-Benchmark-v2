def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start_index = 38
    end_index = 55
    divisible_by_31 = []
    for index, num in enumerate(numbers_list[start_index:end_index + 1], start_index):
        if num % 31 == 0:
            divisible_by_31.append(num)
    return divisible_by_31