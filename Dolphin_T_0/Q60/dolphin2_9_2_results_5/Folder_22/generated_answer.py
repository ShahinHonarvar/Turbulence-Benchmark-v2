def all_left_right_truncatable_prime(numbers):

    def is_left_and_right_truncatable_prime(n):
        primes = {2, 3, 5, 7}
        for digit in map(int, str(n)):
            if digit == 0:
                return False
            n = n.lstrip(str(digit)).rstrip(str(digit))
            if n == '':
                continue
            if int(n) in primes and n[-1] in str(primes):
                primes.add(int(n))
            else:
                return False
        return True
    x = numbers[85]
    return sorted(filter(is_left_and_right_truncatable_prime, range(2, x + 1)))