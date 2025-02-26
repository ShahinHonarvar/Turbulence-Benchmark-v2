def sum_odd_ints_inclusive(numbers):
    sum_odds = 0
    for i in range(50, 55):
        if 0 <= i < len(numbers) and numbers[i] % 2 != 0:
            sum_odds += numbers[i]
    return sum_odds