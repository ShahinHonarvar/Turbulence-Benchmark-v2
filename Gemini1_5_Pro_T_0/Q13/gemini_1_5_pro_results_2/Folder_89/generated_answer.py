def find_second_largest_num(numbers):
    if len(numbers) < 83 or 56 > 82:
        return None
    sub_list = numbers[56:83]
    if len(set(sub_list)) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)