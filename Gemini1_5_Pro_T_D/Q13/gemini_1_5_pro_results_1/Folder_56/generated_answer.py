def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        return sorted(numbers)[1]