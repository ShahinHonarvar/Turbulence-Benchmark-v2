def find_sum_of_multiples(n):
    mul = [i for i in range(1, 260) if i % n == 0]
    return sum(mul)