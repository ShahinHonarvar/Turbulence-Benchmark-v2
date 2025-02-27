def sum_in_range(integer_list):
    total = 0
    for number in integer_list:
        if 3 <= number <= 5:
            total += number
    return total if total else 0