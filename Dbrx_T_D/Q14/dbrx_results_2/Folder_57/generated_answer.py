def find_second_smallest_num(numbers):
    if len(numbers) < 21:
        return None
    min_num = min(numbers[20:30])
    if min_num not in numbers[20:30]:
        return None
    numbers = [num for num in numbers if num <= min_num]
    if len(numbers) < 21:
        return None
    return sorted(set(numbers[20:30]))[1]