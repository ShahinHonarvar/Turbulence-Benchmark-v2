def sum_of_divisors_in_range(N):
    result = 0
    for i in range(4, 9):
        if N % i == 0:
            result += i
    return result