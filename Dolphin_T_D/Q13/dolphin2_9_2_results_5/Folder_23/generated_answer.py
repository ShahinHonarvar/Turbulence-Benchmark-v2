def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    s_slice = numbers[52:72]
    s_slice.sort(reverse=True)
    second_largest = s_slice[1] if len(s_slice) > 1 else None
    return second_largest