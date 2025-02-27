def all_left_right_truncatable_prime(numbers):
    x = numbers[64]

    def is_truncatable_prime(num):
        if num <= 1 or '0' in str(num):
            return False
        s = str(num)
        for i in range(len(s)):
            if int(s[i:]) not in primes or int(s[:len(s) - i]) not in primes:
                return False
        return True
    primes = set([2])
    for i in range(3, x + 1, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    result = []
    for p in primes:
        if is_truncatable_prime(p):
            result.append(p)
    result.sort(reverse=True)
    return result