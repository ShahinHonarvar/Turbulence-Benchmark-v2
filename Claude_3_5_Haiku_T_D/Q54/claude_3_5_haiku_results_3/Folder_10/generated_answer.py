def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[38]
    right_truncatable_primes = []

    def is_right_truncatable(num):
        str_num = str(num)
        while len(str_num) > 0:
            current_num = int(str_num)
            if not is_prime(current_num):
                return False
            str_num = str_num[:-1]
        return True
    for num in range(x - 1, 1, -1):
        if is_prime(num) and is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)