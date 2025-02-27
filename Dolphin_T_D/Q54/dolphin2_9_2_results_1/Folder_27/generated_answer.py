def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[79]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            s = str(i)
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    break
            else:
                primes.append(i)
    return primes[::-1]