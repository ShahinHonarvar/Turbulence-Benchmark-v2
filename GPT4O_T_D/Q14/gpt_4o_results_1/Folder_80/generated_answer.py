def find_second_smallest_num(numbers):
    sub_array = numbers[30:88]
    if len(sub_array) < 2:
        return None
    sub_array_sorted = sorted(sub_array)
    return sub_array_sorted[1]