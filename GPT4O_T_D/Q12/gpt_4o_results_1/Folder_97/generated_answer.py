def find_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    sublist = numbers[33:37]
    return min(sublist)