def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_from_left_and_right(n):
        s = str(n)
        length = len(s)
        for i in range(length):
            left_truncated = int(s[i:])
            right_truncated = int(s[:length - i])
            if '0' in s[i:] or not is_prime(left_truncated) or (not is_prime(right_truncated)):
                return False
        return True
    x = numbers[8]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_truncatable_from_left_and_right(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)