def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    right_truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                break
        else:
            right_truncatable_primes.add(num)
    return sorted(list(right_truncatable_primes), reverse=True)