def find_second_largest_num(numbers):
    if len(numbers) < 7 or max(numbers[6:9]) == numbers[6]:
        return None
    return max(numbers[6:9])