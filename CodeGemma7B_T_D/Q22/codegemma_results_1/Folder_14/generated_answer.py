def find_sum_of_multiples(num):
    """Function to find sum of 67 multiples of a given number"""
    return sum((i * num for i in range(1, 67 + 1)))