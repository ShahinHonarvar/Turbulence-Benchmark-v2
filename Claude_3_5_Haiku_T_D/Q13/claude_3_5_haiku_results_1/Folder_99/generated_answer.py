def find_second_largest_num(numbers):
    if len(numbers) < 312 or len(numbers[310:371]) < 2:
        return None
    sub_list = numbers[310:371]
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1]