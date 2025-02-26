def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[36]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp = num
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                is_truncatable = False
                break
        if is_truncatable:
            temp_str = str(num)
            while len(temp_str) > 1:
                temp_str = temp_str[1:]
                if not is_prime(int(temp_str)):
                    is_truncatable = False
                    break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)