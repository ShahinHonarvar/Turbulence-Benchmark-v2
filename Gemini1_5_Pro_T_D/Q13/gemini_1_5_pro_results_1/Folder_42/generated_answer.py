def find_second_largest_num(numbers):
    if len(numbers) < 30 or len(numbers) < 80:
        return None
    sub_list = numbers[29:80]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]