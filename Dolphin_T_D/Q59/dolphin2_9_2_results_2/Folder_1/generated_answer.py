def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                truncatable = True
                for i in range(len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(num)
    primes.sort(reverse=True)
    return primes