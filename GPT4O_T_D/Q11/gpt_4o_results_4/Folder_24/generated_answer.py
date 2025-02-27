def find_largest_num(numbers):
    if len(numbers) < 96:
        return None
    return max(numbers[74:96])