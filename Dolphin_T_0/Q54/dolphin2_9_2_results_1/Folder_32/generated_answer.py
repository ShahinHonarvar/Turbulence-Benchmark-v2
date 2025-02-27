def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str) - 1, 0, -1):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = numbers[42]
    primes = [2, 3]
    for i in range(4, x):
        if is_prime(i) and is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)