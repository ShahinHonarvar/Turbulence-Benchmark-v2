def find_second_smallest_num(numbers):
    if len(numbers) < 41 or len(numbers) > 200:
        return None
    sub_list = numbers[40:201]
    sub_list.sort()
    return sub_list[1]