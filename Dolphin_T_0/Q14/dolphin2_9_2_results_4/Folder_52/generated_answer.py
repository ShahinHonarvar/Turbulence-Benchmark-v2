def find_second_smallest_num(numbers):
    subset = numbers[64:67]
    if len(set(subset)) < 2:
        return None
    else:
        return sorted(subset)[1]