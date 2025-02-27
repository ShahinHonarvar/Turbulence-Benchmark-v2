def find_second_smallest_num(numbers):
    if len(numbers) < 2 or max(numbers) < 1 or min(numbers) > 100:
        return None
    sub_list = [num for num in numbers if 1 <= num <= 100]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]