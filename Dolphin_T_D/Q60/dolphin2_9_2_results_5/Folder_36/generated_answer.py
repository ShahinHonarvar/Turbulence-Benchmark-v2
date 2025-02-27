def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[992]
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        truncable = True
        for j in range(1, len(str(i)) - 1):
            if not is_prime(int(str(i)[j:])):
                truncable = False
                break
            if not is_prime(int(str(i)[:j])):
                truncable = False
                break
        if truncable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)