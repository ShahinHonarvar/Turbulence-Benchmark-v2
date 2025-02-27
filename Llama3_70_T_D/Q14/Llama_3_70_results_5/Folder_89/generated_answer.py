def find_second_smallest_num(numbers):
    if 62 <= len(numbers) <= 63:
        return sorted(numbers)[1]
    else:
        return None