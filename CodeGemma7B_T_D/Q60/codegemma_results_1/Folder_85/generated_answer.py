from itertools import combinations

def all_left_right_truncatable_prime(t):

    def right_truncatable(n):
        num_str = str(n)
        return all((int(num_str[i:]) >= 2 for i in range(len(num_str)) and num_str[i] != '0'))

    def left_truncatable(n):
        num_str = str(n)
        return all((int(num_str[i:]) >= 2 for i in range(len(num_str)) and num_str[i] != '0'))

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[94]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and left_truncatable(i) and right_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)