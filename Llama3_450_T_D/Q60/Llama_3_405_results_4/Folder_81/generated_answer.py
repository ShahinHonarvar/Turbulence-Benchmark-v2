def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        is_truncatable_prime = True
        for i in range(len(num_str)):
            truncated_num_str = num_str[i:]
            if not is_prime(int(truncated_num_str)):
                is_truncatable_prime = False
                break
            if len(truncated_num_str) > 1:
                truncated_num_str = truncated_num_str[:-1]
                if not is_prime(int(truncated_num_str)):
                    is_truncatable_prime = False
                    break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return truncatable_primes