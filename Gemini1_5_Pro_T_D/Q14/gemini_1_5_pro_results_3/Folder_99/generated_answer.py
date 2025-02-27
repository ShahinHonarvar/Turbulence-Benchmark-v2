def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    else:
        sliced_list = numbers[608:610]
        if sliced_list[0] < sliced_list[1]:
            return sliced_list[1]
        else:
            return sliced_list[0]