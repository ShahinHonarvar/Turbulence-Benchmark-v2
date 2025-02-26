def find_second_largest_num(numbers):
    if len(numbers) < 58 or len(numbers[56:58]) < 2:
        return None
    return sorted(numbers[56:58], reverse=True)[1]