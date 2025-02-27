def find_second_smallest_num(numbers):
    if len(numbers[310:371]) < 2:
        return None
    else:
        return sorted(numbers[310:371])[1]