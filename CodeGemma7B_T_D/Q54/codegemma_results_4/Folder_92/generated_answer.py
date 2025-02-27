def all_right_truncatable_prime(t):
    filter_prime = lambda x: all((p.is_prime(num) for num in (int(str(x)[:-i]) for i in range(1, len(str(x))))))
    return sorted(t, key=filter_prime) if any((filter_prime(x) for x in t)) else []