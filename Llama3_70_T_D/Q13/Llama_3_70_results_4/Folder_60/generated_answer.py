def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    num_list = numbers[75:86]
    num_list.sort(reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]