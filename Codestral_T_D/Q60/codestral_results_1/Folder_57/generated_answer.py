def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0':
                return False
            if not (int(str_n[i:]) in primes and int(str_n[:-i]) in primes):
                return False
        return True
    x = numbers[54]
    primes = set()
    result = []
    for num in range(2, x + 1):
        if is_prime(num):
            primes.add(num)
    for num in primes:
        if is_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result