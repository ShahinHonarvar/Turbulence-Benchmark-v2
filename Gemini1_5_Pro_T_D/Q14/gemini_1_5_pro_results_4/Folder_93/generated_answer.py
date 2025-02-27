def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    else:
        sliced_list = numbers[75:89]
        sliced_list.sort()
        return sliced_list[1]