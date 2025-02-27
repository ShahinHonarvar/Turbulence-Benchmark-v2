def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[67]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            for i in range(1, len(num_str)):
                if num_str[i] == '0' or not is_prime(int(num_str[i:])):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)