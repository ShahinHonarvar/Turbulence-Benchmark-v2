def sum_odd_ints_inclusive(numbers):
    odd_integers = [num for num in numbers[90:201] if num % 2 != 0]
    return sum(odd_integers) if odd_integers else 0