def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        sliced_list = numbers[56:58]
        sliced_list.sort()
        return sliced_list[1]