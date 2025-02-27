def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[30]
    primes = []
    for i in range(2, x):
        num_str = str(i)
        if '0' in num_str:
            continue
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                break
            num_str = num_str[1:]
        else:
            primes.append(i)
    return primes