def sum_in_range(integer_list):
    total = 0
    for i in integer_list:
        if 38 <= i <= 81:
            total += i
    return total if total else 0