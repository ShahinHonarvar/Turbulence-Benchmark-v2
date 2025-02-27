def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[429]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            trunc = num
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc = int(trunc / 10)
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes