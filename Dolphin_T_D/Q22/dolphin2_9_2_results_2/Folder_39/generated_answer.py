def find_sum_of_multiples(n):
    multiples_sum = 0
    for i in range(1, 94):
        multiples_sum += i * n
    return multiples_sum