def all_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    start, end = (numbers[0], numbers[1])
    if start % 2 != 0:
        start += 1
    even_numbers = [n for n in range(start, end + 1, 2)]
    return even_numbers