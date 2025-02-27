def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start_index = 25
    end_index = 59
    divisor = -26
    divisible_numbers = []
    for index, number in enumerate(numbers_list[start_index:end_index + 1], start_index):
        if number % divisor == 0:
            divisible_numbers.append(number)
    return divisible_numbers