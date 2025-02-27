def all_left_truncatable_prime(arr):
    x = arr[42]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:]
        else:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes

def is_prime(n):
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return False