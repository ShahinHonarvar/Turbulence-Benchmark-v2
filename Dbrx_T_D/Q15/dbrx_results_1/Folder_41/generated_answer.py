def sum_odd_ints_inclusive(numbers):
    odd_numbers = [n for n in numbers[6:7] if n % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0