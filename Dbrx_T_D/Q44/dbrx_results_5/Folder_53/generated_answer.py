def composite_nums_between_indices(numbers):
    try:
        index_222 = numbers.index(222)
    except ValueError:
        return set()
    if len(numbers) - 1 - index_222 < 222:
        return set()
    return {num for num in numbers[index_222:222 + 222 + 1] if not num % 2 and num != 2 or (num / 2 % 1 == 0 and num != 3)}