def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    start = numbers[21:98]
    if len(start) < 2:
        return None
    first, second = (max(start[0], start[1]), min(start[0], start[1]))
    for num in start[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    if second == first:
        return None
    else:
        return second