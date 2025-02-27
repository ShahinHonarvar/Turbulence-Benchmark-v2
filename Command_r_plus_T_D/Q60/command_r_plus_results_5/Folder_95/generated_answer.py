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
        left_prime = right_prime = True
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_prime = right_prime = False
                break
        if left_prime and right_prime:
            left_right_primes.append(num)
    return sorted(left_right_primes)