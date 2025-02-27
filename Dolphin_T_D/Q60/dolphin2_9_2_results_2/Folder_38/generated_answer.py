def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    truncable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        length = len(str_num)
        while length > 1:
            if length > 2 and str_num[0] == '0':
                break
            left_trunc = int(str_num[1:])
            right_trunc = int(str_num[:-1])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                break
            if length == 2:
                truncable_primes.append(num)
            length -= 1
    return sorted(truncable_primes)