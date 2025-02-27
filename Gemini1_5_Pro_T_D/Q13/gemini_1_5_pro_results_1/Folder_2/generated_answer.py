def find_second_largest_num(numbers):
    if len(numbers) < 40 or len(numbers[15:40]) == 1:
        return None
    sub_list = numbers[15:40]
    sub_list.sort()
    return sub_list[-2]