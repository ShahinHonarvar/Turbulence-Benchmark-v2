def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[i:length - i])):
                return False
        return True
    x = numbers[22]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)