def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min(numbers[1:100])
    return min_num if numbers.count(min_num) > 1 else None