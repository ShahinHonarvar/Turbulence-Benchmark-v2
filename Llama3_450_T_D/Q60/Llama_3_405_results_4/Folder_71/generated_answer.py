def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[22]
    truncatable_primes = set()
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i - 1]))):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)