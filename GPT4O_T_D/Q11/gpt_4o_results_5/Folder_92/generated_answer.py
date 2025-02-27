def find_largest_num(numbers):
    if len(numbers) >= 2:
        return max(numbers[0], numbers[1])
    elif numbers:
        return numbers[0]
    return None