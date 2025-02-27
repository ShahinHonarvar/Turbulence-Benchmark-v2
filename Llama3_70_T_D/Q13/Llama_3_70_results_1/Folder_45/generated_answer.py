def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    temp_list = numbers[30:201]
    temp_list.sort(reverse=True)
    if len(temp_list) < 2:
        return None
    return temp_list[1]