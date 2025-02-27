def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[15:52]
    if len(set(sub_list)) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)