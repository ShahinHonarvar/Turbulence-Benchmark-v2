def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    sub_list = numbers[31:73]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(sub_list)
    return unique_sorted[1]