def find_second_largest_num(numbers):
    section = numbers[33:56]
    if len(section) < 2:
        return None
    max1 = max(section)
    section.remove(max1)
    if len(section) < 2:
        return None
    max2 = max(section)
    return max2