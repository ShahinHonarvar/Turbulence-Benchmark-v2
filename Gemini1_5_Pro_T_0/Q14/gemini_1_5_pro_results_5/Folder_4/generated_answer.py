def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    else:
        sliced_list = numbers[70:85]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]