def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[3]
    primes = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = str(num)
            while len(temp) > 1:
                temp = temp[1:-1]
                if not is_prime(int(temp)):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)