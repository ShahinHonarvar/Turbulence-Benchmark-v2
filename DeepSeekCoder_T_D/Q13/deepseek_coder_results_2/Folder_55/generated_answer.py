def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 10:
        return None
    sub_list = numbers[:11]
    sub_list.sort(reverse=True)
    return sub_list[1]