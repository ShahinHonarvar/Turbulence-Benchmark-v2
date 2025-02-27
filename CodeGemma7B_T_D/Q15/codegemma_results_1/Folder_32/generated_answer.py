def sum_odd_ints_inclusive(numlist):
    items = numlist[21:98]
    odds = [x for x in items if x % 2 != 0]
    if odds == []:
        return 0
    else:
        return sum(odds)