def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    else:
        sliced_list = numbers[30:49]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]