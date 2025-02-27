def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 87 - 25 + 1:
        return None
    first_half = numbers[25:63]
    second_half = numbers[63:88]
    first_half_max = max(first_half)
    second_half_max = max(second_half)
    if first_half_max > second_half_max:
        first_half.remove(first_half_max)
        return max(first_half_max, max(first_half))
    else:
        second_half.remove(second_half_max)
        return max(second_half_max, max(second_half))