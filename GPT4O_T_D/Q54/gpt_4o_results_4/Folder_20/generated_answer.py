def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(upper_limit):

    def is_right_truncatable_prime(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    primes = []
    for number in range(2, upper_limit):
        if is_right_truncatable_prime(number):
            primes.append(number)
    return primes

def all_right_truncatable_prime(numbers):
    if len(numbers) > 100:
        x = numbers[100]
        primes = right_truncatable_primes(x)
        return sorted(primes, reverse=True)
    return []