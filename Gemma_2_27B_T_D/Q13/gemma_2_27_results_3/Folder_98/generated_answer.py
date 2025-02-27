def find_second_largest_num(numbers):
    if len(numbers[:7]) < 2:
        return None
    return sorted(numbers[:7])[-2]