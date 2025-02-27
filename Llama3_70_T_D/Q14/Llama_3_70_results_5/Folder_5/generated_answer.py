def find_second_smallest_num(numbers):
    try:
        target_numbers = sorted(numbers[3:6])
        return target_numbers[1]
    except IndexError:
        return None