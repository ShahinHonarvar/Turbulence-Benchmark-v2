def find_second_largest_num(numbers):
    sub_list = numbers[56:83]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list, default=None)
    return second_largest