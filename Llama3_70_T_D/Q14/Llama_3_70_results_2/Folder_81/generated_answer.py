def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    second_smallest = min(numbers[10:101])
    numbers[10:101].remove(second_smallest)
    if numbers[10:101]:
        return min(numbers[10:101])
    else:
        return None