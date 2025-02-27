def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[10:67]
    if len(set(sub_list)) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list)
    return second_largest