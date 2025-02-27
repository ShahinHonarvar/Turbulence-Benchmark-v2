def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 7:
        return None
    sub_list = numbers[:8]
    max_num = max(sub_list)
    sub_list.remove(max_num)
    return max(sub_list)