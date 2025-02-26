def sum_odd_ints_inclusive(numbers):
    sum_odds = 0
    for i in range(533, 606):
        if i < len(numbers) and numbers[i] % 2 != 0:
            sum_odds += numbers[i]
    return sum_odds