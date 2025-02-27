def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    num_list = numbers[62:79]
    num_list.sort()
    if len(num_list) < 2:
        return None
    return num_list[1]