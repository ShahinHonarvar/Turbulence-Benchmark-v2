def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(2, x + 1):
        if all_left_right_truncatable_prime_helper(num):
            primes.append(num)
    return primes

def all_left_right_truncatable_prime_helper(num):
    if int(str(num)[-1]) == 0 or int(str(num)[0]) == 0:
        return False
    i = 0
    while len(str(num)) != i + 1:
        num = int(str(num)[i + 1:-(i + 1)])
        i += 1
        if str(num)[-1] == '0' or str(num)[0] == '0' or (not is_prime(num)):
            return False
    return is_prime(num)