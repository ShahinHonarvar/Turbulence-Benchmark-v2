def find_sum_of_multiples(n):
    if n <= 0:
        return 'Input should be a positive integer.'
    else:
        multiples = [i for i in range(1, 30) if i % n == 0]
        return sum(multiples)