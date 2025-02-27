def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62:
        return None
    second_largest = max(set(numbers[16:62]) - {max(numbers[16:62])})
    if second_largest == max(numbers[16:62]):
        return None
    else:
        return second_largest