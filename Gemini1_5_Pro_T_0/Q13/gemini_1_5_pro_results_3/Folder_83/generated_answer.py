def find_second_largest_num(numbers):
    if len(numbers) < 91 or 90 > len(numbers):
        return None
    sub_list = numbers[90:91]
    if len(set(sub_list)) != len(sub_list):
        return None
    if len(sub_list) == 1:
        return None
    else:
        return sorted(sub_list)[-2]