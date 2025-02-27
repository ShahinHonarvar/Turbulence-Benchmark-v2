def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n or len(str_n) < 2:
            return False
        for i in range(len(str_n))[:-1]:
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i - 1])):
                return False
        return True
    primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)