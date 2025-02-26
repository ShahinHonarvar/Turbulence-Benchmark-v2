def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 7:
        return None
    sub_list = numbers[0:8]
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1]