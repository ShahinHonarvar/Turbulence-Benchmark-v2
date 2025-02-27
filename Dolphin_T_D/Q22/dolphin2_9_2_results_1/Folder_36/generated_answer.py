def find_sum_of_multiples(n):
    _sum = 0
    for i in range(1, 339):
        _sum += n * i
    return _sum