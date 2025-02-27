def find_sum_of_multiples(num):
    """Finds the sum of the first 20 positive multiples of the given integer."""
    sum = 0
    for i in range(1, 21):
        sum += i * num
    return sum