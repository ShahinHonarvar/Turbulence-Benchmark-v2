def all_left_truncatable_prime(numbers):
    x = numbers[177]

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) not in prime_numbers:
                return False
        return True
    prime_numbers = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    left_truncatable_primes = []
    for number in prime_numbers:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes