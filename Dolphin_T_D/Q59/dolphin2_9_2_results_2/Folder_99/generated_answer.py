def all_left_truncatable_prime(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    x = numbers[758]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        n = num
        while n != 0:
            if not is_prime(n):
                break
            n //= 10
        if n == 0:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)