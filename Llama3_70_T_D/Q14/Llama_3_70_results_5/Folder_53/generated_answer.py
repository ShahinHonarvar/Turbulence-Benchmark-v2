def find_second_smallest_num(numbers):
    return sorted(numbers[1:101])[1] if len(numbers[1:101]) > 1 else None