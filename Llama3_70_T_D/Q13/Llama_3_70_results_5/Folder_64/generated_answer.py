def find_second_largest_num(numbers):
    if len(numbers[:5]) < 2:
        return None
    return sorted(set(numbers[:5]), reverse=True)[1]