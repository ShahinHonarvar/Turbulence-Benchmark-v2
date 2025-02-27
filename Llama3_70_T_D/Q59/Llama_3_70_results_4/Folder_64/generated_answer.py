def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[4]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and num not in left_truncatable_primes:
            i = num
            while i > 0:
                if not is_prime(i):
                    break
                left_truncatable_primes.append(i)
                i = int(str(i)[1:])
            else:
                left_truncatable_primes.append(num)
    return sorted(list(set(left_truncatable_primes)))