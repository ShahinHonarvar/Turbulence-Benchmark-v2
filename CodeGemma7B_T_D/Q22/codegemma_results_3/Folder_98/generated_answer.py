def find_sum_of_multiples(n):
    if n <= 0:
        return None
    multiples = [i for i in range(1, 11) if i % n == 0]
    return sum(multiples)