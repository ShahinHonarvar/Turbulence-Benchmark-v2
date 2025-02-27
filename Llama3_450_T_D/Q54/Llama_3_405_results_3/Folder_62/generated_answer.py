def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    right_truncatable_primes = set()
    for num in range(10, x):
        if is_prime(num):
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    break
            else:
                right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes))