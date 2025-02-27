def find_sum_of_multiples(N):
    sum_multiples = 0
    for i in range(1, 26):
        sum_multiples += i * N
    return sum_multiples