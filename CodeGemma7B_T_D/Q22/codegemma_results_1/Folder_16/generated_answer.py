def find_sum_of_multiples(num):
    """This function takes one argument, a positive integer, and returns the sum of the first 255 possitive multiples of the given integer."""
    sum = 0
    for i in range(1, 256):
        sum += i * num
    return sum