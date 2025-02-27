def find_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    return min(numbers[70:85])