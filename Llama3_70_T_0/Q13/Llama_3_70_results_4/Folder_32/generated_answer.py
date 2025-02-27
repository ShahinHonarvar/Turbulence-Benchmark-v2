def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    else:
        return sorted(numbers[20:98])[-2]