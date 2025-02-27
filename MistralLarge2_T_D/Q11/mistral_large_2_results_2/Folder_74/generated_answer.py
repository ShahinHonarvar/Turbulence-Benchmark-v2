def find_largest_num(numbers):
    if len(numbers) > 78:
        return max(numbers[17:79])
    else:
        return None