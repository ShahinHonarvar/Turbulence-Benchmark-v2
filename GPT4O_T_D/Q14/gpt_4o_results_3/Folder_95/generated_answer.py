def find_second_smallest_num(numbers):
    if len(numbers) < 86 or len(numbers[75:86]) < 2:
        return None
    sub_list = sorted(numbers[75:86])
    return sub_list[1]