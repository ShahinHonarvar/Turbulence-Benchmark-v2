def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    second_smallest = min(numbers[1:6])
    if second_smallest == min(numbers):
        numbers.remove(second_smallest)
        if len(numbers) < 2:
            return None
        second_smallest = min(numbers[1:6])
    return second_smallest