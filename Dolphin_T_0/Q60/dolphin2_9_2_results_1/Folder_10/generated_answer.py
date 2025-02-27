def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if not '0' in str_num:
            for i in range(len(str_num) - 1, 0, -1):
                left = int(str_num[:i])
                right = int(str_num[i + 1:])
                if not is_prime(left) or not is_prime(right) or len(str_num) == 2:
                    break
                primes.append(num)
    return sorted(primes, reverse=True)