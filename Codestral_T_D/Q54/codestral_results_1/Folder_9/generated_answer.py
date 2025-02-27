def all_right_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []
    for num in range(2, x):
        is_truncatable_prime = True
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[:-i - 1])
            if truncated_num < 2 or not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True