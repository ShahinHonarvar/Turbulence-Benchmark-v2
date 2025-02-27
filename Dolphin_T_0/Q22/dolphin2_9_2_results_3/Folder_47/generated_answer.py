def find_sum_of_multiples(num):
    """Returns the sum of the first 38 positive multiples of a given positive integer"""
    return sum((num * i for i in range(1, 39)))