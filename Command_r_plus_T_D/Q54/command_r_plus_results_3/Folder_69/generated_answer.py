def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(n):
        primes = []
        for i in range(10 ** len(str(n)), 10, -1):
            if str(n)[:len(str(i))] == str(i) and is_prime(n):
                primes.append(n)
                break
            n //= 10
        return primes
    x = numbers[760]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable_primes.extend(generate_right_truncatable_primes(i))
    right_truncatable_primes = sorted(list(set(right_truncatable_primes)), reverse=True)
    return [i for i in right_truncatable_primes if i < x]