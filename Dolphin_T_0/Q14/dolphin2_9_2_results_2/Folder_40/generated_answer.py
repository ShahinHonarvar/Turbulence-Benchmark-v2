def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    elif len(numbers) == 3:
        return sorted(numbers)[1]
    else:
        return sorted(numbers[:3])[1]