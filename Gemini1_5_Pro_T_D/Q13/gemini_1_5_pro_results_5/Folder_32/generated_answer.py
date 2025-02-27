def find_second_largest_num(numbers):
    if len(numbers) < 23 or 97 >= len(numbers):
        return None
    sub_list = numbers[21:98]
    sorted_list = sorted(sub_list)
    return sorted_list[-2]