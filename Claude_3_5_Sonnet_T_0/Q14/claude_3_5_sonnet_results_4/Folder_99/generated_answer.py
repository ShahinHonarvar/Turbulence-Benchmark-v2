def find_second_smallest_num(numbers):
    sublist = numbers[608:610]
    if len(sublist) < 2:
        return None
    return max(sublist)