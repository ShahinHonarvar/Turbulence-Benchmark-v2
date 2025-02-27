def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(start):
    primes = []
    for num in range(2, start + 1):
        if is_prime(num) and '0' not in str(num):
            if len(str(num)) == 2 or len(str(num)) == 1:
                primes.append(num)
            else:
                left = int(str(num)[1:])
                right = int(str(num)[:-1])
                if is_prime(left) and is_prime(right):
                    primes.append(num)
    return primes