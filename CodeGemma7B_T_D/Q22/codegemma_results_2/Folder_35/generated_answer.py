def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 117) if i % n == 0]
    return sum(multiples)