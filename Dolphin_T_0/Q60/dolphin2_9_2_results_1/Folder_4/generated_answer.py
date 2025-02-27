def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = int_tuple[96]
    primes = []
    for num in range(x, 0, -1):
        if is_prime(num):
            str_num = str(num)
            if all((is_prime(int(str_num[i:j])) for i in range(len(str_num)) for j in range(i + 1, len(str_num) + 1))):
                primes.append(num)
    return sorted(primes, reverse=True)