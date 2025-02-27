def find_second_smallest_num(numbers):
    if 66 >= len(numbers) or 93 >= len(numbers):
        return None
    num_list = sorted(numbers[66:94])
    if len(num_list) < 2:
        return None
    else:
        return num_list[1]