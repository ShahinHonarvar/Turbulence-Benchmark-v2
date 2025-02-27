def find_second_smallest_num(numbers):
    try:
        target_numbers = sorted(numbers[82:87])
        if len(target_numbers) > 1:
            return target_numbers[1]
    except IndexError:
        pass
    return None