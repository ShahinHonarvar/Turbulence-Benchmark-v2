def find_second_smallest_num(numbers):
    if len(numbers[64:67]) < 2:
        return None
    return sorted(numbers[64:67])[1]