def find_divisors_in_range(integer):
    if integer % 2 == 0:
        if integer // 2 >= 70 and integer // 2 <= 72:
            return [integer // 2]
    if integer % 3 == 0:
        if integer // 3 >= 70 and integer // 3 <= 72:
            return [integer // 3]
    if integer % 5 == 0:
        if integer // 5 >= 70 and integer // 5 <= 72:
            return [integer // 5]
    if integer % 7 == 0:
        if integer // 7 >= 70 and integer // 7 <= 72:
            return [integer // 7]
    return []