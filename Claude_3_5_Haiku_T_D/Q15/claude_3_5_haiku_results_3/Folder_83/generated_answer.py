def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return 0
    odd_integers = [num for num in numbers[90:201] if num % 2 != 0]
    return sum(odd_integers)