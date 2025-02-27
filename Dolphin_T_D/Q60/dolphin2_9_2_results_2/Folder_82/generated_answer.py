def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    nums = list(tup)
    x = nums[69]
    primes = [i for i in range(x, 1, -1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        str_num = str(prime)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num[1:-1])):
                break
            str_num = str_num[1:-1]
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)