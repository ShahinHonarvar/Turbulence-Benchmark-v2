def all_odd_ints_inclusive(numbers):
    odds = []
    for number in numbers:
        if number >= 60 and number <= 60:
            if number % 2 != 0:
                odds.append(number)
    return odds if odds else []