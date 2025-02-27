def find_sum_of_multiples(n):
    a = 1
    b = n * 100
    result = 0
    while a <= b:
        result += a
        a += n
    return result