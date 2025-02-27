def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    else:
        sliced_list = numbers[35:50]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]