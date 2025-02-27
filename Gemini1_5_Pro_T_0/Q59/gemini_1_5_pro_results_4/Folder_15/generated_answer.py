def all_left_truncatable_prime(numbers):
    x = numbers[6]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 1:
            return True
        if '0' in str(n):
            return False
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            else:
                return is_left_truncatable_prime(int(str(n)[1:]))
        else:
            return False
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result