def all_odd_ints_inclusive(lst):
    results = []
    for num in lst:
        if num % 2 != 0 and 0 <= num <= 2:
            results.append(num)
    return results