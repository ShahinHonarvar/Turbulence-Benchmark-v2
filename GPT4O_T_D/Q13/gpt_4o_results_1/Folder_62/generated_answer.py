def find_second_largest_num(numbers):
    sublist = numbers[91:100]
    if len(sublist) < 2:
        return None
    sorted_unique = sorted(set(sublist), reverse=True)
    return sorted_unique[1] if len(sorted_unique) > 1 else None