def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    portion = numbers[12:93]
    sorted_portion = sorted(set(portion))
    if len(sorted_portion) < 2:
        return None
    return sorted_portion[1]