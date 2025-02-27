def sum_even_ints_inclusive(numbers):
    if not numbers:
        return 0
    lower_bound = min(0, numbers[0])
    upper_bound = max(0, numbers[0])
    for num in numbers[1:]:
        if num % 2 == 0:
            upper_bound = max(upper_bound, num)
        else:
            lower_bound = max(lower_bound, num)
    if lower_bound > upper_bound:
        return 0
    return sum((x for x in range(lower_bound, upper_bound + 1) if x % 2 == 0))