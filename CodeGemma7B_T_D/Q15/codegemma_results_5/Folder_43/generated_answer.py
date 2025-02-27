def sum_odd_ints_inclusive(int_list: list[int]) -> int:
    """Calculates the sum of all odd integers from index 68 to index 86, inclusive."""
    total = 0
    for i in range(68, 87):
        if int_list[i] % 2 != 0:
            total += int_list[i]
    return total if total else 0