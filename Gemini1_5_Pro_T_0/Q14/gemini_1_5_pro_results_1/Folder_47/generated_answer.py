def find_second_smallest_num(numbers):
    if len(numbers) < 64 or len(numbers) < 23:
        return None
    else:
        sliced_list = numbers[22:64]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]