def helper_is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    primes = []
    for num in range(11, x + 1):
        if '0' not in str(num) and helper_is_prime(num):
            left_truncatable = True
            right_truncatable = True
            left_num = str(num)
            right_num = str(num)
            while len(left_num) > 1:
                left_num = left_num[1:]
                if not helper_is_prime(int(left_num)):
                    left_truncatable = False
                    break
            while len(right_num) > 1:
                right_num = right_num[:-1]
                if not helper_is_prime(int(right_num)):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(num)
    return primes