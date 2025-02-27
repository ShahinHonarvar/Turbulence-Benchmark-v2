def find_second_smallest_num(lst):
    if 71 < len(lst):
        numbers = lst[52:72]
        numbers.sort()
        if len(numbers) > 1:
            return numbers[1]
    return None