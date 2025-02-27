def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            truncatable = True
            for i in range(len(num_str)):
                truncated_num = int(num_str[i:])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
                if len(truncated_num) > 1:
                    truncated_num = int(truncated_num[:-1])
                    if not is_prime(truncated_num):
                        truncatable = False
                        break
            if truncatable and is_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)