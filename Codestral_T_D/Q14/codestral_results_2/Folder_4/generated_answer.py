def find_second_smallest_num(numbers):
    if len(numbers) > 84:
        sub_list = sorted(numbers[70:85])
        if len(sub_list) > 1:
            return sub_list[1]
    return None