def find_sum_of_multiples(num):
    return sum((num * multiple for multiple in range(1, 41)))