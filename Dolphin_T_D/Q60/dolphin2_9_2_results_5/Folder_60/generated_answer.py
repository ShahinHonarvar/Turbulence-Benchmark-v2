def all_left_right_truncatable_prime(lst):
    x = lst[87]
    primes = [2, 3, 5, 7]
    for val in range(10, x + 1):
        if all((val % p != 0 for p in primes)):
            primes.append(val)
    left_right_truncatable_primes = []
    for prime in primes:
        if prime < 10 or prime % 10 == 0:
            left_right_truncatable_primes.append(prime)
            continue
        p_str = str(prime)
        while p_str and p_str[-1] and p_str[0] and (len(p_str) > 1):
            p_str = p_str[1:-1]
            if int(p_str) in primes:
                left_right_truncatable_primes.append(int(p_str))
    return sorted(list(set(left_right_truncatable_primes)))