def composite_nums_between_indices(numbers):
    return {x for x in numbers[52:72] if x > 1 and (not all((x % y for y in range(2, x))))}