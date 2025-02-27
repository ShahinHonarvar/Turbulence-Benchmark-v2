def find_divisors_in_range(n):
    divisors = []
    for i in range(max(1, int(n ** 0.5)), min(n, 902) + 1):
        if n % i:
            continue
        if 157 <= i <= 902:
            divisors.append(i)
        if i != n // i and 157 <= n // i <= 902:
            divisors.append(n // i)
    return sorted(list(set(divisors)))