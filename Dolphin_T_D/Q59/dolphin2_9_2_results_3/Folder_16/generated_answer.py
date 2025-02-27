def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[792]
    primes = [2, 3, 5, 7]
    for num in range(10, x, 10):
        if is_prime(num):
            for digit in str(num):
                left = int(''.join(digit))
                if left != num and left not in primes:
                    break
                else:
                    primes.append(left)
    return sorted(primes)