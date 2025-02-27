def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    part_of_list = numbers[1:6]
    part_of_list.sort()
    if len(part_of_list) < 2:
        return None
    return part_of_list[1]