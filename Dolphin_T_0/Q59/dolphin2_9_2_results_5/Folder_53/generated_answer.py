def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(a):
    x = a[86]
    primes = list()
    for num in range(x, 1, -1):
        if is_prime(num):
            temp = num
            while temp:
                if is_prime(temp):
                    temp //= 10
                else:
                    break
            if temp == 0:
                primes.append(num)
    return sorted(primes, reverse=True)