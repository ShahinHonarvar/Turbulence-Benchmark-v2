def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    else:
        sliced_list = numbers[50:55]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]