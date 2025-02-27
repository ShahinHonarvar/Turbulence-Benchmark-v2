def find_second_smallest_num(num_list):
    if len(num_list) < 95:
        return None
    numbers = sorted(num_list[75:95])
    if len(numbers) < 2:
        return None
    return numbers[1]