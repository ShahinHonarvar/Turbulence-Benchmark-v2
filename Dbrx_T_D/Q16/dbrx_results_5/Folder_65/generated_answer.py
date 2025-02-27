def sum_even_ints_inclusive(lst):
    start_index = min(max(56, 0), len(lst) - 1)
    end_index = min(max(98, 0), len(lst) - 1)
    even_sums = sum((x for x in lst[start_index:end_index + 1] if x % 2 == 0))
    return even_sums if even_sums else 0