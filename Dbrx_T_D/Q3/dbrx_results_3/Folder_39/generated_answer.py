def all_pos_ints_inclusive(numbers):
    if len(numbers) < 31:
        return []
    sub_list = numbers[20:31]
    return [num for num in sub_list if num > 0]