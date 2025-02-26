def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 10:
        return None
    slice_list = numbers[10:11]
    if not slice_list:
        return None
    return slice_list[0]