def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    number = numbers[263]
    if is_prime(number):
        return prime_set
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            if is_prime(i):
                prime_set.add(i)
            number //= i
    if number > 1:
        prime_set.add(number)
    return prime_set