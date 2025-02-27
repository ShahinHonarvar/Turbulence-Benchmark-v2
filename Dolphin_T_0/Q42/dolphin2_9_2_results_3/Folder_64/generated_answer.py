def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_set = set()
    target_num = numbers[1]
    for i in range(2, target_num + 1):
        if is_prime(i) and target_num % i == 0:
            prime_set.add(i)
    return prime_set