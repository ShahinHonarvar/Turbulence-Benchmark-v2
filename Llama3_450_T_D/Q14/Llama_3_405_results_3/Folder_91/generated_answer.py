def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        return sorted(numbers[:6])[1]