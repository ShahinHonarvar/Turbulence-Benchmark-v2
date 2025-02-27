def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    else:
        sliced_list = numbers[608:610]
        sliced_list.sort()
        return sliced_list[1]