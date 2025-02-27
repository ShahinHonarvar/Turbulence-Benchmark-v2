def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num = min(numbers[:3])
    second_smallest_num = min(filter(lambda x: x > min_num, numbers[:3]))
    if second_smallest_num:
        return second_smallest_num
    else:
        return None