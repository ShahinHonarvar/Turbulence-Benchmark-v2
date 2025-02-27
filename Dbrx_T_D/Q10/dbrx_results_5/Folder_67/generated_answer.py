def all_odd_ints_exclusive(numbers):
    odds = []
    for i in range(len(numbers)):
        if i >= 49 and i < 74 and (numbers[i] % 2 != 0):
            odds.append(numbers[i])
    return odds