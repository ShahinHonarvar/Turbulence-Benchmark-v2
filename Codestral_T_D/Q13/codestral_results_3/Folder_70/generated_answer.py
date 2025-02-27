def find_second_largest_num(numbers):
    sliced_list = numbers[28:33]
    if len(sliced_list) < 2:
        return None
    else:
        max_num = max(sliced_list)
        return max([num for num in sliced_list if num < max_num])