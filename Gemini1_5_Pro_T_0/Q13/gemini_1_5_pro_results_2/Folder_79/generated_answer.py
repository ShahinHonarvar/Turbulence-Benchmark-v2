def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        return sorted(numbers[4:5])[0]