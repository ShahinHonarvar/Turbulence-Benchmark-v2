def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        current_num = num
        while current_num > 9:
            current_num = int(str(current_num)[1:])
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
        current_num = num
        while current_num > 9:
            current_num = int(str(current_num)[:-1])
            if not is_prime(current_num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes