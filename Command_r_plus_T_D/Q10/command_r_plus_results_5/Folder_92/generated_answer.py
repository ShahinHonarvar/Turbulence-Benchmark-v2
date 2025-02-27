def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = []
    for index, number in enumerate(numbers_list):
        if index > 1:
            break
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers