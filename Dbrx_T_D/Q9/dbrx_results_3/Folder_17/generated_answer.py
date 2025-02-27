def all_odd_ints_inclusive(lst):
    if len(lst) >= 79:
        start, end = (62, 78)
        odds = [num for num in lst[start:end + 1] if num % 2 != 0]
        return odds
    else:
        return []