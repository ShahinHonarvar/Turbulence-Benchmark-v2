def sum_odd_ints_inclusive(l):
    oddeven = [a % 2 for a in l[52:72]]
    odds = [b for b in oddeven if b == 1]
    if not odds:
        return 0
    else:
        return sum(odds)