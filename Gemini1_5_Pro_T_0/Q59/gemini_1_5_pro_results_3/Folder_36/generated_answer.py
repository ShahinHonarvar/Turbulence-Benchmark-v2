def all_left_truncatable_prime(numbers):
    x = numbers[992]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 1:
            return True
        if '0' in str(n) or n < 10:
            return False
        if all((i != '1' for i in str(n))):
            for i in range(len(str(n))):
                if int(str(n)[i:]) % 2 == 0:
                    return False
        else:
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result