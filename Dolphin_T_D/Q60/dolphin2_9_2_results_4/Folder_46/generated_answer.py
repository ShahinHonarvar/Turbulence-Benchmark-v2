def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            while len(str(num)) > 1:
                num = int(str(num)[1:-1])
                if not is_prime(num):
                    break
            else:
                primes.append(num)
    return sorted(primes)