def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[784]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num or not is_prime(num):
            continue
        while True:
            if len(str_num) == 2:
                primes.append(num)
                break
            if not is_prime(int(str_num[1:-1])) or '0' in str_num[1:-1]:
                break
            str_num = str_num[1:-1]
    return sorted(primes)