def all_right_truncatable_prime(n):
    return sorted((n[70] // 10 ** i for i in range(1, int(n[70] ** 0.5) + 1) if all((n[70] % 10 ** i == 0 or n[70] % 10 ** i == 9 for j in range(1, i + 1)))))