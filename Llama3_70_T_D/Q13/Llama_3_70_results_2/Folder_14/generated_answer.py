def find_second_largest_num(numbers):
    try:
        return sorted(numbers[5:8])[-2]
    except IndexError:
        return None