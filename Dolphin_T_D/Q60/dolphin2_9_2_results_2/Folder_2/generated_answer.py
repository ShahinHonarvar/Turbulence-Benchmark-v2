def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[618]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if '0' not in str(n):
            while n != 0 and n != 1 and (n != 2) and (n != 3) and (n != 4):
                n = int(str(n)[1:-1])
                if not is_prime(n):
                    break
            if n != 0 and n != 1 and (n != 2) and (n != 3) and (n != 4) and (n != 5) and (n != 7):
                left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)