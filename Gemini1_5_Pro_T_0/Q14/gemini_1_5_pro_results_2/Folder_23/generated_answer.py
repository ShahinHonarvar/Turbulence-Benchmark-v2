def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 21:
        return None
    else:
        sliced_list = numbers[19:93]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]