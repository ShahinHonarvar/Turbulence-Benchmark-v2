def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[746]
    prime_set = set()
    i = 2
    while i * i <= num:
        if num % i == 0 and is_prime(i):
            prime_set.add(i)
            num //= i
        else:
            i += 1
    if num > 1:
        prime_set.add(num)
    return prime_set