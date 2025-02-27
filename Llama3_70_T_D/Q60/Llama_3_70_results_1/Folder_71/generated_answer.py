def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            truncatable_prime = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)