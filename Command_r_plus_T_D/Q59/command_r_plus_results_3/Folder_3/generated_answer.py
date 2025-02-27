def all_left_truncatable_prime(limit_tup):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(num):
        if num < 10 and is_prime(num):
            yield num
        for i in range(1, num // 10 + 1):
            new_num = num - 10 * i
            if new_num > 0 and is_prime(new_num) and (str(new_num)[0] != '0'):
                yield from generate_left_truncatable_primes(new_num)
    limit = limit_tup[100]
    left_truncatable_primes = []
    for num in range(2, limit):
        if is_prime(num):
            left_truncatable = all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)))))
            if left_truncatable:
                left_truncatable_primes.append(num)
    left_truncatable_primes.extend(generate_left_truncatable_primes(23))
    return sorted(left_truncatable_primes)