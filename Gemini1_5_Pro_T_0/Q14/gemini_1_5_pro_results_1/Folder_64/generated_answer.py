def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    sub_list = numbers[0:5]
    sorted_list = sorted(sub_list)
    return sorted_list[1]