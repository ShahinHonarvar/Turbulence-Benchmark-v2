def find_divisors_in_range(x):
    if x % 2 == 0:
        if x % 3 == 0:
            if x % 5 == 0:
                if x % 7 == 0:
                    return [x]
    return []