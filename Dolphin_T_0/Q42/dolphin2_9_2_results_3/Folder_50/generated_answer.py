def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    prime_set = set()
    num = numbers[40]
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
    return prime_set