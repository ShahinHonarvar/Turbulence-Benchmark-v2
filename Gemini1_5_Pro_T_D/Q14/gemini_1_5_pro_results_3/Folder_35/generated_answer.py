def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sliced_list = numbers[15:40]
    min_num = min(sliced_list)
    if sliced_list.count(min_num) > 1:
        return min_num
    sliced_list.remove(min_num)
    if len(sliced_list) == 0:
        return None
    return min(sliced_list)