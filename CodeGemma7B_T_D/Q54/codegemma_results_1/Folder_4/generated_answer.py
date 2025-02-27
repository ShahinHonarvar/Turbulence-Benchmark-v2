def all_right_truncatable_prime(x):
    right_truncatable_primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(x):
        numstr = str(num)
        for i in range(len(numstr)):
            if is_prime(int(numstr[:len(numstr) - i])):
                right_truncatable_primes.append(int(numstr[:len(numstr) - i]))
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes