def find_second_largest_num(numbers):
    if len(numbers[:7]) < 2:
        return None
    sorted_nums = sorted(numbers[:7])
    return sorted_nums[-2]