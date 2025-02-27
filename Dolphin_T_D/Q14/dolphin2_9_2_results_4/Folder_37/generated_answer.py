def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    for i in range(5, 8):
        if i >= len(numbers):
            return None
        if numbers[i] != min(numbers[i - 5:i]):
            return numbers[i]
    return None