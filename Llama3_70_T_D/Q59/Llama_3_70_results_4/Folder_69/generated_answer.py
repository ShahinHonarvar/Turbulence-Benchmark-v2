def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' not in str(num):
            prime = True
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    prime = False
                    break
            if prime and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)