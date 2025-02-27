def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_primes = []
    for num in numbers:
        if num < 10:
            continue
        str_num = str(num)
        left_prime = is_prime(int(str_num[1:])) if str_num[0] != '0' else False
        right_prime = is_prime(int(str_num[:-1])) if str_num[-1] != '0' else False
        if is_prime(num) and left_prime and right_prime:
            left_right_primes.append(num)
    return sorted(left_right_primes)

def get_left_right_primes_up_to_x(x):
    if x < 10:
        return []
    return all_left_right_truncatable_prime(range(10, x + 1))