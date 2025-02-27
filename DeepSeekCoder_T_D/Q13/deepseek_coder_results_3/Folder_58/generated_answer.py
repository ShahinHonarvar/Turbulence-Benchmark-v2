def find_second_largest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    sub_list = numbers[209:557]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]