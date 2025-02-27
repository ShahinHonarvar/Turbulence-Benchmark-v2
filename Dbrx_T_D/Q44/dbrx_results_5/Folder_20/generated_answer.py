def composite_nums_between_indices(numbers):
    try:
        start, end = (74, 95)
        return {num for num in numbers[start:end + 1] if num > 1 and num % 2 == 0 and (num ** 0.5).is_integer()}
    except IndexError:
        return set()