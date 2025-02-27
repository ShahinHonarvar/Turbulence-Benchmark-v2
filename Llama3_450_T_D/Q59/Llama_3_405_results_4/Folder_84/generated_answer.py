def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[630]
    left_truncatable_primes = []
    for i in range(11, x):
        s = str(i)
        if '0' in s:
            continue
        if is_prime(i):
            truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)