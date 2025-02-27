def sum_odd_ints_inclusive(numbers):
    sum_of_odds = 0
    for i in range(max(59, 0), min(98, len(numbers))):
        if numbers[i] % 2 != 0:
            sum_of_odds += numbers[i]
    return sum_of_odds