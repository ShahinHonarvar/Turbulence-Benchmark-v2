def find_second_largest_num(numbers):
    if len(numbers) <= 92:
        return None
    return sorted(set(numbers[12:93]), reverse=True)[1]