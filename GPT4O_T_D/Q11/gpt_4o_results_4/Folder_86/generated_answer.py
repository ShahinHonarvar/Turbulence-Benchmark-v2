def find_largest_num(numbers):
    if len(numbers) >= 35:
        return max(numbers[31:35])
    else:
        return None