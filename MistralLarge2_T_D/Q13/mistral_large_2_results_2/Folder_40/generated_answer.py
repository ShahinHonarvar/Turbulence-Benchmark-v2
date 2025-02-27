def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers[:3])
    numbers[:3].remove(first_largest)
    if numbers[:2]:
        return max(numbers[:2])
    return None