def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sub_list = numbers[:9]
    sub_list.sort(reverse=True)
    return sub_list[1]