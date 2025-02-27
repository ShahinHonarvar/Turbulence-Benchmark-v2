def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[466]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            prime = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[j:])):
                    prime = False
                    break
            if prime:
                primes.append(i)
    primes.sort(reverse=True)
    return primes