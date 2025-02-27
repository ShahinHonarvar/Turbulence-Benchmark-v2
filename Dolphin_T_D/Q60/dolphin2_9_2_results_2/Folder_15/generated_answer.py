def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[6]
    left_right_truncatable_prime = []
    for i in range(2, x + 1):
        if '0' not in str(i):
            if is_prime(i):
                trunc = i
                while trunc > 9:
                    if not is_prime(trunc // 10) or not is_prime(trunc % 10):
                        break
                    trunc //= 10
                else:
                    left_right_truncatable_prime.append(i)
    return sorted(left_right_truncatable_prime, reverse=True) or []