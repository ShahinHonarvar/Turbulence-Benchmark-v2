def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])
    x = numbers[93]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = truncate_left(num)
        if num == 0:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)