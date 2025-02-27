def find_sum_of_multiples(inv_int):
    sum = 0
    for i in range(1, 187):
        sum += i * inv_int
    return sum