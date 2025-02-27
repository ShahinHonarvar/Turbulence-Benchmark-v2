def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for i in range(x, 0, -1):
        str_i = str(i)
        while len(str_i) > 2:
            if str_i[0] == '0' or str_i[-1] == '0' or (not is_prime(int(str_i[1:-1]))):
                break
            else:
                str_i = str_i[1:-1]
        else:
            if is_prime(i):
                primes.append(i)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True