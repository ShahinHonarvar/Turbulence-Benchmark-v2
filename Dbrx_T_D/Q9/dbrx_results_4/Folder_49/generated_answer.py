def all_odd_ints_inclusive(numbers):
    odds_in_range = []
    for i in range(len(numbers)):
        if i >= 80 and i <= 200:
            if numbers[i] % 2 != 0:
                odds_in_range.append(numbers[i])
    return odds_in_range