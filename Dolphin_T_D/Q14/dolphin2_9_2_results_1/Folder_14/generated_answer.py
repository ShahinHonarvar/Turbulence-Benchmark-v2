def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        section = numbers[8:10]
        section.sort()
        return section[1] if len(section) > 1 else None