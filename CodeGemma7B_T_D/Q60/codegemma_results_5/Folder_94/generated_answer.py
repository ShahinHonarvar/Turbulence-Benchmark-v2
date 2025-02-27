def all_left_right_truncatable_prime(t):
    x = t[42]
    left_right_truncatable_prime = []
    for i in range(2, x + 1):
        if is_prime(i) and (not is_zero(i)) and is_left_right_truncatable_prime(i):
            left_right_truncatable_prime.append(i)
    return sorted(left_right_truncatable_prime)