def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = set()
    for _ in range(222, 223):
        num = numbers[_]
        if num < 2:
            continue
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors.add(i)
        if num > 1:
            prime_factors.add(num)
    return prime_factors