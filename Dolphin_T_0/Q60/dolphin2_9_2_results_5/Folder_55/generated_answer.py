def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[73]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            k = i
            while True:
                if len(str(k)) == 1 or (len(str(k)) == 2 and is_prime(k)):
                    primes.append(i)
                    break
                if not is_prime(k):
                    break
                if str(k)[0] == '0':
                    k = int(str(k)[1:])
                else:
                    k = int(str(k)[1:-1])
    return sorted(primes, reverse=True)