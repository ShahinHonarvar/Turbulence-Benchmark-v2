def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        prime = True
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:-i or None])
            if not is_prime(truncated_num):
                prime = False
                break
        if prime and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)