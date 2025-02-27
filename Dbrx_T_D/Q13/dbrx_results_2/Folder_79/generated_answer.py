def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sub_list = numbers[4:5]
    largest_num = max(sub_list)
    sub_list.remove(largest_num)
    second_largest_num = max(sub_list)
    if second_largest_num < numbers[4] and second_largest_num != largest_num:
        return second_largest_num
    else:
        return None