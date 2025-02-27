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

    def is_truncatable(p):
        s = str(p)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:length - i])):
                return False
        return True
    x = numbers[38]
    primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)