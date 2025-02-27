def find_second_largest_num(numbers):
    if len(numbers[29:94]) < 2:
        return None
    else:
        sorted_numbers = sorted(numbers[29:94])
        return sorted_numbers[-2]