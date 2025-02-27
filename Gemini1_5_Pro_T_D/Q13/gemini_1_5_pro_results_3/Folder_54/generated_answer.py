def find_second_largest_num(numbers):
    if len(numbers) < 56 or len(numbers[34:56]) == 1:
        return None
    else:
        sliced_list = numbers[34:56]
        sliced_list.sort()
        return sliced_list[-2]