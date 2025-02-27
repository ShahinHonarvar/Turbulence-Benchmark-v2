def sum_odd_ints_inclusive(numbers):
    odd_ints = [n for n in numbers[43:52] if n % 2 != 0]
    return sum(odd_ints) if odd_ints else 0