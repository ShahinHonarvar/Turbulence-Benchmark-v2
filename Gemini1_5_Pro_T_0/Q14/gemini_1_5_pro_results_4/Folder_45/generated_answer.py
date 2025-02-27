def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 30:
        return None
    sub_list = numbers[30:201]
    sorted_list = sorted(sub_list)
    return sorted_list[1]