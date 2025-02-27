def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    else:
        sliced_list = numbers[20:201]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]