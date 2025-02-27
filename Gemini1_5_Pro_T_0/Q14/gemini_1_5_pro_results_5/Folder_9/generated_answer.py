def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 70:
        return None
    sub_list = numbers[70:201]
    if len(set(sub_list)) == 1:
        return None
    temp = sorted(sub_list)
    return temp[1]