def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101:
        return None
    first_half = numbers[10:51]
    second_half = numbers[51:101]
    first_half_numbers = set(first_half)
    second_half_numbers = set(second_half)
    if len(first_half_numbers) < 2 and len(second_half_numbers) < 2:
        return None
    first_half_sorted = sorted(list(first_half_numbers))
    second_half_sorted = sorted(list(second_half_numbers))
    if len(first_half_sorted) < 2:
        return None if len(second_half_sorted) < 2 else second_half_sorted[-2]
    if len(second_half_sorted) < 2:
        return first_half_sorted[-2]
    if first_half_sorted[-1] > second_half_sorted[-1]:
        return first_half_sorted[-2]
    return second_half_sorted[-2]