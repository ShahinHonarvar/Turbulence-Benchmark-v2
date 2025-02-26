def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[36]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[1:]
                if not is_prime(int(str_num)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)