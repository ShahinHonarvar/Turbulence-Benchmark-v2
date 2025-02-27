def all_odd_ints_inclusive(numbers):
    odds = []
    for i in range(74, 96):
        if i >= len(numbers):
            break
        if numbers[i] % 2 != 0:
            odds.append(numbers[i])
    return odds