def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[i:length - i])):
                return False
        return True
    x = numbers[86]
    left_right_truncatable_primes = []
    if x < 10:
        return []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes