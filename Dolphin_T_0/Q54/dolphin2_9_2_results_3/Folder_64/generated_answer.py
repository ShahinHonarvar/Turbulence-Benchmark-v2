def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[4]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if is_prime(num):
            flag = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    flag = False
                    break
            if flag:
                primes.append(num)
    return sorted(primes)