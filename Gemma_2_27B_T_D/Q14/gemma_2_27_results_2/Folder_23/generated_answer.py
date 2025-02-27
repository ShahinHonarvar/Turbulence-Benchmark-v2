def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 19 not in range(len(numbers)) or 92 not in range(len(numbers)):
        return None
    sub_list = numbers[19:93]
    sorted_list = sorted(sub_list)
    return sorted_list[1]