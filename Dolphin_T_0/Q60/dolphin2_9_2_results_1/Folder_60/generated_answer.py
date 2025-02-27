def all_left_right_truncatable_prime(numbers_tuple):

    def check_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers_tuple[87]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        z = len(str_i)
        while z > 1:
            if check_prime(int(str_i[1:z - 1])):
                z -= 1
            else:
                break
        if z == 1 and check_prime(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes