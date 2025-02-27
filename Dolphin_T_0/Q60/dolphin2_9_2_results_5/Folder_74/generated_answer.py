def all_left_right_truncatable_prime(numbers):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[36]
    primes = []
    for num in range(x, 1, -1):
        if _is_prime(num):
            string_num = str(num)
            if '0' in string_num:
                continue
            while len(string_num) > 2:
                if not _is_prime(int(string_num[1:-1])):
                    break
                string_num = string_num[1:-1]
            if len(string_num) == 2 and _is_prime(int(string_num)):
                primes.append(num)
    return sorted(primes)