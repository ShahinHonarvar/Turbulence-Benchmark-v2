def find_second_smallest_num(numbers):
    sub_array = numbers[56:67]
    if len(sub_array) < 2:
        return None
    sorted_sub_array = sorted(sub_array)
    return sorted_sub_array[1]