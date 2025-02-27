def all_right_truncatable_prime(t):
    return sorted([i for i in range(t[91]) if all((i % j for j in range(2, int(str(i)[-2::-1]) + 1)))])