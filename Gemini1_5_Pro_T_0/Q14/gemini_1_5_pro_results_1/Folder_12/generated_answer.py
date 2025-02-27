def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    else:
        sliced_list = numbers[31:73]
        sorted_list = sorted(sliced_list)
        return sorted_list[1]