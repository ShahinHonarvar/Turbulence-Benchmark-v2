def find_divisors_in_range(integer):
    if integer % 46 == 0 or integer % 65 == 0:
        return [integer // 46, integer // 65]
    else:
        return []