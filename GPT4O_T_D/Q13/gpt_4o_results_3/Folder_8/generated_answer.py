def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None
    sub_array = numbers[23:24]
    if len(sub_array) < 2:
        return None
    sorted_sub_array = sorted(sub_array)
    return sorted_sub_array[-2]