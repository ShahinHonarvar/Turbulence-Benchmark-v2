def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[370]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 2:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
            if str_num == '':
                left_right_truncatable_primes.append(num)
                break
    return sorted(left_right_truncatable_primes, reverse=True)