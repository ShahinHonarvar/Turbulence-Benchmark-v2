def find_second_largest_num(numbers):
    if 26 <= len(numbers) <= 52:
        return sorted(numbers[26:53], reverse=True)[1]
    return None