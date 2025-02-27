def find_second_smallest_num(numbers):
    target_numbers = sorted(numbers[70:85])
    if len(target_numbers) < 2:
        return None
    return target_numbers[1]