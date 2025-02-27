def sum_odd_ints_inclusive(lst):
    if len(lst) < 66:
        return 'List is too short. Please provide a list with length at least 66.'
    else:
        odds = [i for i in lst[56:67] if i % 2 != 0]
        return sum(odds) if odds else 0