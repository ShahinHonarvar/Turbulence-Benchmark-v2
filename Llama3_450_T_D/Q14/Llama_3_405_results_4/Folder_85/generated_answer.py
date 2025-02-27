def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    return sorted(numbers[:7])[1]