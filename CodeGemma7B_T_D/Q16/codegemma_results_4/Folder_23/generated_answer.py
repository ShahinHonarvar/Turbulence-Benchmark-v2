def sum_even_ints_inclusive(list_of_ints):
    """Sums all even integers from index 52 to index 71, inclusive."""
    total = 0
    for i in range(52, 72):
        if list_of_ints[i] % 2 == 0:
            total += list_of_ints[i]
    if total == 0:
        return 0
    else:
        return total