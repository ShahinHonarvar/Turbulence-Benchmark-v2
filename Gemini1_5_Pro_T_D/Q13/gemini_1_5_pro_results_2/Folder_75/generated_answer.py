def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sub_list = numbers[56:58]
    if sub_list[0] > sub_list[1]:
        return sub_list[1]
    else:
        return sub_list[0]