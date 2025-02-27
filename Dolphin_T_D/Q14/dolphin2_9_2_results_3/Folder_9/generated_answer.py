def find_second_smallest_num(lst):
    if not lst or len(lst) < 2:
        return None
    numbers = [num for num in lst[70:201]]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]