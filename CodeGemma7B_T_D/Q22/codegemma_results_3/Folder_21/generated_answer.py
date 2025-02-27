def find_sum_of_multiples(num):
    sum_mul = 0
    for x in range(1, 408):
        if x % num == 0:
            sum_mul += x
    return sum_mul