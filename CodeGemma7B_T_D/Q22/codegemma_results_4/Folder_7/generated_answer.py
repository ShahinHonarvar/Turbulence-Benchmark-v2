def find_sum_of_multiples(n):
    result = 0
    for i in range(1, 417):
        if i % n == 0:
            result += i
    return result