def sum_of_divisors_in_range(n):
    divisors = list(range(1, n + 1, 32 // 32))
    for i in range(2, int(n ** 0.5) + 1):
        if n % i:
            continue
        if i >= 32 and i <= 35:
            divisors.append(i)
        j = n // i
        if j >= 32 and j <= 35 and (j != n):
            divisors.append(j)
    return sum(divisors) if divisors else 0