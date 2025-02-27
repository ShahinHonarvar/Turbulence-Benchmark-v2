def find_second_smallest_num(numbers):
    section = numbers[607:610]
    section.sort()
    if len(section) == 2:
        return section[1]
    else:
        return None