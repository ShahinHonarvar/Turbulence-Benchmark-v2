def all_left_truncatable_prime(n):
    return sorted(list(set(range(2, n[0] + 1))), reverse=True)