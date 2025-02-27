def sum_odd_ints_inclusive(lst):
    numbers = lst[30:201]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0