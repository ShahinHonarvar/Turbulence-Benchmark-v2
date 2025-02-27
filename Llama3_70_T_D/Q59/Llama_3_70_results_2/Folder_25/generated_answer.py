def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[92]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = str(num)
        is_left_truncatable = True
        for _ in range(len(temp)):
            if not is_prime(int(temp)):
                is_left_truncatable = False
                break
            temp = temp[1:]
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)