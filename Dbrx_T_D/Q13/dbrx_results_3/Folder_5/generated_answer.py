def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 9 or len(numbers) - 1 < 8:
        return None
    sorted_numbers = sorted(set(numbers))
    second_largest_num = sorted_numbers[-2]
    if 8 <= sorted_numbers.index(second_largest_num) <= 9:
        return second_largest_num
    else:
        return None