def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 90:
        return None
    sub_list = numbers[90:201]
    if len(set(sub_list)) == 1:
        return None
    temp = sorted(sub_list)
    return temp[1]