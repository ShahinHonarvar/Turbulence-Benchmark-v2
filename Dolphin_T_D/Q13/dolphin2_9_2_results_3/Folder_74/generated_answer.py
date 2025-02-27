def find_second_largest_num(numbers):
    if 17 <= 78 < len(numbers):
        sublist = numbers[17:78]
        if len(set(sublist)) >= 2:
            unique_sorted = sorted(set(sublist), reverse=True)
            return unique_sorted[1]
    return None