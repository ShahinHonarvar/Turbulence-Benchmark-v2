def all_odd_ints_exclusive(numbers):
    for i in range(743, 867):
        if i >= len(numbers) or not isinstance(numbers[i], int) or numbers[i] % 2 == 0:
            continue
        yield numbers[i]