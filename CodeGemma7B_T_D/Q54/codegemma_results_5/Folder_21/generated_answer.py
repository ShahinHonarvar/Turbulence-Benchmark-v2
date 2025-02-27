def all_right_truncatable_prime(n):
    x = n[175]
    result = list()
    for i in range(2, int(x ** 0.5) + 1):
        if all((j % i != 0 for j in range(i * 2, x + 1, i))):
            result.extend([i] + [j for j in range(i * 10, x + 1, i * 10)])
    return sorted(set(result))