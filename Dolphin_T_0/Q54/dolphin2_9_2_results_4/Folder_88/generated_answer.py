def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[93]
    primes = [2]
    for num in range(3, x):
        if is_prime(num):
            trunc = str(num)
            while len(trunc) > 1:
                if not is_prime(int(trunc)):
                    break
                trunc = trunc[:-1]
            else:
                primes.append(num)
    return sorted(primes)