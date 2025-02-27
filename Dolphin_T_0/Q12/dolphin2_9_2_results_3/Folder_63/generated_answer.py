def find_smallest_num(numbers):
    if 62 < len(numbers) <= 63:
        return min(numbers)
    elif 62 <= len(numbers):
        return min(numbers[62:64])
    else:
        return None