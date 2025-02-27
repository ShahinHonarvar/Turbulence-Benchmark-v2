def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[767]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_left_truncatable = True
        num_str = str(num)
        for i in range(1, len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes