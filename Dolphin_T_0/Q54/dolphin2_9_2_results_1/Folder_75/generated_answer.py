def all_right_truncatable_prime(num_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = num_tuple[41]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            for digit in str(i)[::-1][1:]:
                if not is_prime(int(str(i).replace(digit, ''))):
                    right_truncatable = False
                    break
            if right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)