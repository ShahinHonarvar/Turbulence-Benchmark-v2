def all_right_truncatable_prime(numbers):
    x = numbers[630]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable_prime = True
        str_num = str(num)
        for i in range(len(str_num) - 1, 0, -1):
            if int(str_num[:i]) not in right_truncatable_primes and (not is_prime(int(str_num[:i]))):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime and is_prime(num):
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True