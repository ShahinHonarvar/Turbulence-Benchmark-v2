def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 465) if i % n == 0]
    sum_of_multiples = sum(multiples)
    return sum_of_multiples