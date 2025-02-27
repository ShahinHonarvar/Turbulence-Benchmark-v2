def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if '0' in str_n or not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    x = numbers[91]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes)