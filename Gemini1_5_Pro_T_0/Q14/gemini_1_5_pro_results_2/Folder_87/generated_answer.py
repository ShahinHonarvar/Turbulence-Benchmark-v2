def find_second_smallest_num(numbers):
    if len(numbers) < 89 or len(numbers) < 23:
        return None
    else:
        sliced_list = numbers[22:89]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]