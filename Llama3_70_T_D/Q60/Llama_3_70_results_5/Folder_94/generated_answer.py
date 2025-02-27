def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(t):
    x = t[43]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i):
            temp = str(i)
            temp_prime = True
            while len(temp) > 1:
                if not is_prime(int(temp)):
                    temp_prime = False
                    break
                temp = temp[1:-1]
            if temp_prime and is_prime(int(temp)):
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)