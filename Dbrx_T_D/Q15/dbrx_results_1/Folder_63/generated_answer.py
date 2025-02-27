def sum_odd_ints_inclusive(lst):
    if not isinstance(lst, list) or len(lst) < 89:
        raise ValueError('Input must be a list of at least 89 integers')
    sum_of_odds = 0
    for i in range(22, 89):
        if lst[i] % 2 != 0:
            sum_of_odds += lst[i]
    return sum_of_odds