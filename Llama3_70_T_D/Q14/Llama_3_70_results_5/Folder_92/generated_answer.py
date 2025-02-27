def find_second_smallest_num(numbers):
    if len(numbers[:2]) < 2:
        return None
    return sorted(numbers[:2])[1]