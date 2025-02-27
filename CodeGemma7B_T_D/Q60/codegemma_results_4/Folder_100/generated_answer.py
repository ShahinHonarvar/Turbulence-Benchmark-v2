def all_left_right_truncatable_prime(tuple1):
    x = tuple1[26]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_truncatable_primes(num):
        result = []
        if len(str(num)) == 1 and is_prime(num):
            result.append(num)
            return result
        if str(num)[0] == '0':
            return result
        left_trunc = int(str(num)[1:])
        if is_prime(left_trunc):
            result = find_truncatable_primes(left_trunc)
        if str(num)[-1] == '0':
            return result
        right_trunc = int(str(num)[:-1])
        if is_prime(right_trunc):
            result.extend(find_truncatable_primes(right_trunc))
        return result
    truncatable_primes = find_truncatable_primes(x)
    truncatable_primes.sort()
    return truncatable_primes