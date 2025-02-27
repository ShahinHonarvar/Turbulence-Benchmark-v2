def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sub_list = numbers[0:2]
    if len(sub_list) < 2:
        return None
    first, second = (sub_list[0], sub_list[1]) if sub_list[0] > sub_list[1] else (sub_list[1], sub_list[0])
    return second