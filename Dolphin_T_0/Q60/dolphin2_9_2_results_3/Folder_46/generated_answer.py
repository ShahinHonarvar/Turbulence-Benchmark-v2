def all_left_right_truncatable_prime(contiguous_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = contiguous_tuple[33]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and all((is_prime(int(str_num[i:])) and is_prime(int(str_num[:i])) for i in range(1, len(str_num)))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)