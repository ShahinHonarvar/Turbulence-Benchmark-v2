def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    numbers[36:47] = sorted(numbers[36:47], reverse=True)
    return numbers[37]