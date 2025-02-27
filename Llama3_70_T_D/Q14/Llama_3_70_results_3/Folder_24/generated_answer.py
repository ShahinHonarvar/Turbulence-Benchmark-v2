def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    num_list = numbers[23:24]
    if len(num_list) == 1:
        return None
    num_list.sort()
    return num_list[1]