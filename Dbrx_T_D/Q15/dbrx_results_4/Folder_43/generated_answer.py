def sum_odds_inclusive(numbers):
    odds = [n for n in numbers[67:87] if n % 2 != 0]
    return sum(odds) if odds else 0