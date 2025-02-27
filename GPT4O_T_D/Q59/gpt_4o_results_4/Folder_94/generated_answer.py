def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        s = str(num)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[43]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes)