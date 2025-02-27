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

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length - 1):
            left_trunc = int(s[i + 1:])
            right_trunc = int(s[:length - i - 1])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = numbers[77]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)