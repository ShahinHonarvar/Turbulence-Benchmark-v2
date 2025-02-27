def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        count = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                count = count + 1
        if count > 1:
            return False
        else:
            return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if is_prime(int(str_n[i:])) and is_prime(int(str_n[:i])):
                is_truncatable = True
            else:
                return False
        return is_truncatable
    primes = []
    x = numbers[14]
    for n in range(2, x + 1, -1):
        if is_prime(n) and is_truncatable(n):
            primes.append(n)
    return primes