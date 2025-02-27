def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[88]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp_num = str(num)
        is_left_truncatable = True
        for i in range(len(temp_num)):
            if not is_prime(int(temp_num[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)