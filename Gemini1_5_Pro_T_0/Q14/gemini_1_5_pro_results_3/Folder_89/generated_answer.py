def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sub_list = numbers[62:64]
        if sub_list[0] < sub_list[1]:
            return sub_list[1]
        else:
            return sub_list[0]