def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_numbers = []
    for _ in range(2):
        min_num = min(numbers)
        min_numbers.append(min_num)
        numbers.remove(min_num)
    if len(min_numbers) == 1:
        return None
    return sorted(min_numbers)[1]