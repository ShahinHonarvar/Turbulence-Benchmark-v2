from __future__ import generators

def find_sum_of_multiples(n):
    total = 0
    for num in range(1, 49):
        if num % n == 0:
            total += num
    return total