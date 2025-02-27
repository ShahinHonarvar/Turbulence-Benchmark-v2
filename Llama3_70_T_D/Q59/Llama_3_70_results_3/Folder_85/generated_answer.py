def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            temp = str(num)
            is_prime_flag = True
            for i in range(len(temp)):
                if not is_prime(int(temp[i:])):
                    is_prime_flag = False
                    break
            if is_prime_flag:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)