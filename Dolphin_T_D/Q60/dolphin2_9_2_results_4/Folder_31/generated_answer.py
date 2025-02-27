def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        trunc = len(str_num)
        while trunc > 1:
            if check_prime(int(str_num[1:-1])):
                primes.append(num)
                break
            trunc -= 1
    primes.sort(reverse=True)
    return primes