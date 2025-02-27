def find_second_smallest_num(numbers):
    if len(numbers) < 2 or max(numbers) < 1 or min(numbers) > 100:
        return None
    sublist = [num for num in numbers if 1 <= num <= 100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]