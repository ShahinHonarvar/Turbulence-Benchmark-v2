def find_second_smallest_num(numbers):
    if len(numbers) < 201 or min(90, len(numbers) - 1) == max(90, len(numbers) - 1):
        return None
    sliced = numbers[90:201]
    smallest = min(sliced)
    sliced.remove(smallest)
    if len(sliced) == 0:
        return None
    return min(sliced)