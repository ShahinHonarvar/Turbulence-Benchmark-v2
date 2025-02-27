def sum_of_divisors_in_range(num):
    """Function to find the sum of all positive divisors of a given positive integer in the range of 10 to 69, both inclusive."""
    sum_of_divisors = 0
    for i in range(10, 70):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors