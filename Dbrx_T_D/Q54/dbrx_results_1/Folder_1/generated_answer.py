def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def generate_rt_primes(n):
    rt_primes = []
    for i in range(n):
        if is_prime(i):
            rt_primes.append(i)
            num = i
            while num > 9:
                num = remove_last_digit(num)
                if is_prime(num):
                    rt_primes.append(num)
                else:
                    break
    return rt_primes

def all_right_truncatable_prime(t):
    x = t[20]
    rt_primes = generate_rt_primes(x)
    return sorted(list(set(rt_primes)), reverse=True)