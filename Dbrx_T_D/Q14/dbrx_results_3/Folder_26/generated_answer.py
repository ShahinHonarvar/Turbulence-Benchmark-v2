def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62 or len(numbers) < 78:
        return None
    min_num = min(numbers[62:79])
    numbers.remove(min_num)
    second_min_num = min(numbers[62:79])
    return second_min_num