def find_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[5:8]
    return min(sublist)