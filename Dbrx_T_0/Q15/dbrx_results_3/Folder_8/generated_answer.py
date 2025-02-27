def sum_odd_ints_inclusive(numbers):
    start, end = (23, 23)
    odd_ints = [num for num in numbers[start:end + 1] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0