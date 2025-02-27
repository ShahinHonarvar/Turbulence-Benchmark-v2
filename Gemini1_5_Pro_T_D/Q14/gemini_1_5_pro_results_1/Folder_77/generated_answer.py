def find_second_smallest_num(numbers):
    if len(numbers) < 976:
        return None
    else:
        sliced_list = numbers[639:976]
        sliced_list.sort()
        return sliced_list[1]