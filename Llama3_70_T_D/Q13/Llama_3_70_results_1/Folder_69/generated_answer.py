def find_second_largest_num(numbers):
    try:
        return sorted(numbers[32:36])[::-1][1]
    except IndexError:
        return None