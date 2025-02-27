def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    else:
        sub_list = numbers[32:36]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[1]