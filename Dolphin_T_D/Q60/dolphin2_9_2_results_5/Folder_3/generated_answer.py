def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            for i in range(len(str(num)) - 2, -1, -1):
                if not is_prime(int(str(num)[i:])):
                    break
            else:
                primes.append(num)
    return primes