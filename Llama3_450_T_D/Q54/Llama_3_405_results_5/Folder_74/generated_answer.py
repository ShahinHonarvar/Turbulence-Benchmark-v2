def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[36]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            truncatable = True
            for i in range(len(num_str)):
                trunc_str = num_str[:len(num_str) - i]
                trunc_num = int(trunc_str)
                if trunc_num < 2 or not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)