def find_second_smallest_num(numbers):
    if len(numbers[:4]) < 2:
        return None
    smallest_num = min(numbers[:4])
    second_smallest_num = min((i for i in numbers[:4] if i != smallest_num))
    return second_smallest_num