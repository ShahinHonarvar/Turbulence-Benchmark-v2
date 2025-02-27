def find_second_largest_num(numbers):
    if len(numbers) < 976 or len(numbers) < 639:
        return None
    sub_list = numbers[639:976]
    if len(set(sub_list)) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)