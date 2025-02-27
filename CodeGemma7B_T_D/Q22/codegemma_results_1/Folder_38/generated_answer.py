def find_sum_of_multiples(n):
    SumEights = 0
    for i in range(1, 78):
        SumEights += i * n
    return SumEights