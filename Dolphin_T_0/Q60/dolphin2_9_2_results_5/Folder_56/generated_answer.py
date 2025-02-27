def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[30]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            truncation_nums = [int(str_num[i:j]) for i in range(len(str_num)) for j in range(i + 1, len(str_num) + 1)]
            if all(is_prime(num) and all((is_prime(trunc) for trunc in truncation_nums))):
                primes.append(num)
    return sorted(primes)