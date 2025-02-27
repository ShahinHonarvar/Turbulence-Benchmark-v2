def find_sum_of_multiples(k):
    multiples = [i for i in range(0, 78) if i % k == 0]
    return sum(multiples)