def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[67]
    truncatable_primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            left_truncated = str_num[1:]
            right_truncated = str_num[:-1]
            if left_truncated and right_truncated and is_prime(int(left_truncated)) and is_prime(int(right_truncated)):
                truncatable = True
                while len(str_num) > 2:
                    str_num = str_num[1:-1]
                    if not (str_num and is_prime(int(str_num))):
                        truncatable = False
                        break
                if truncatable:
                    truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)