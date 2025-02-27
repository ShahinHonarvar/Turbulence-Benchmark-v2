def find_sum_of_multiples(num):
    """Calculates the sum of the first 29 multiples of a given number."""
    sum = 0
    for i in range(1, 30):
        sum += i * num
    return sum