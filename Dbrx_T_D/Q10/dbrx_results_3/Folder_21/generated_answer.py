def all_odd_ints_exclusive(numbers):
    odds = []
    for i in range(743, 867):
        if i < len(numbers) and numbers[i] % 2 != 0:
            odds.append(numbers[i])
    return odds