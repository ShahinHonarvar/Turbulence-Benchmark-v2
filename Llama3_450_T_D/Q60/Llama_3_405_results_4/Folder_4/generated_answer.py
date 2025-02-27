def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[96]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_truncated = str_num
        right_truncated = str_num
        is_truncatable_prime = True
        while len(left_truncated) > 1 and len(right_truncated) > 1:
            left_truncated = left_truncated[1:]
            right_truncated = right_truncated[:-1]
            if not is_prime(int(left_truncated)) or not is_prime(int(right_truncated)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)