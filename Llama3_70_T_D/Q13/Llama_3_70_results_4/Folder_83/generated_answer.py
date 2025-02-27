def find_second_largest_num(numbers):
    try:
        return sorted(numbers[90:91])[1]
    except IndexError:
        return None