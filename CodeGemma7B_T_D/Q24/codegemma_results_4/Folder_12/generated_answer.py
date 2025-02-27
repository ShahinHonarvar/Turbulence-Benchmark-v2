import math

def sum_of_divisors_in_range(n):
    if n > 0:
        sum = 0
        for i in range(13, 62):
            if n % i == 0:
                sum += i
        if sum == 0:
            return 0
        else:
            return sum
    else:
        return 'Error: Please provide a positive integer.'