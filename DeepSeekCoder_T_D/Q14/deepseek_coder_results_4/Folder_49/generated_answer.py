def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 80:
        return None
    sub_list = numbers[80:201]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]