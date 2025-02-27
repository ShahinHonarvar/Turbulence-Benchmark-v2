def find_second_smallest_num(numbers):
    if len(numbers[1:101]) < 2:
        return None
    return sorted(set(numbers[1:101]))[1]