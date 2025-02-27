def all_right_truncatable_prime(numbers):

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

    def right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    if len(numbers) <= 126:
        return []
    x = numbers[126]
    truncatable_primes = []
    for num in range(2, x):
        if right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)