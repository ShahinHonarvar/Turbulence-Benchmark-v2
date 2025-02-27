def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num) - 1):
            if not is_prime(int(str_num[i + 1:])) or not is_prime(int(str_num[:len(str_num) - (i + 1)])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes