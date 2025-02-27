def all_odd_ints_exclusive(numbers):
    for i in range(len(numbers)):
        if i < 10 or i >= 11:
            continue
        elif i == 10 or i == 11:
            if numbers[i] % 2 != 0:
                return [numbers[i]]
    return []