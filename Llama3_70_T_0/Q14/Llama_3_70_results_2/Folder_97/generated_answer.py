def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    second_smallest = min(numbers[31:35])
    numbers[31:35].remove(second_smallest)
    if len(numbers[31:35]) == 0:
        return None
    return min(numbers[31:35])