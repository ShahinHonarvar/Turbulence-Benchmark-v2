def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = numbers[91]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            while i > 1:
                if is_prime(i):
                    i = int(i / 10)
                else:
                    break
            else:
                result.append(i)
    return result