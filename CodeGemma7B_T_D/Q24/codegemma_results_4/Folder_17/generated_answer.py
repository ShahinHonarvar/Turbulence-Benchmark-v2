def sum_of_divisors_in_range(n):
    n = (n // 2 + 1) * (n // 10 + 1) * (n // 20 + 1) * (n // 50 + 1) * (n // 100 + 1) * (n // 200 + 1) * (n // 500 + 1) * (n // 1000 + 1) * (n // 2000 + 1) * (n // 5000 + 1)
    ns = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i >= 10 and i <= 69:
                ns += i
        if n % i == 0:
            if i >= 10 and i <= 69:
                ns += n / i
    if ns == 0:
        return 0
    else:
        return int(ns)