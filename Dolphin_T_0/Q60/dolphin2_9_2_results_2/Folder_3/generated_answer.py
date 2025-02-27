def all_left_right_truncatable_prime(t):
    x = t[100]
    left_right_truncatable_primes = []
    for num in range(1, x + 1):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                while len(str_num) > 1:
                    str_num = str_num[1:-1]
                    if not is_prime(int(str_num)):
                        break
                else:
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True