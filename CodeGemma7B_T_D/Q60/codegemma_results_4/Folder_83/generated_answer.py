def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_last_two_digits(n):
        return n % 100
    result = []
    for i in range(25, x + 1):
        if is_prime(i) and (not '0' in str(i)):
            j = i
            while j >= 10 and is_prime(j):
                last_two_digits = get_last_two_digits(j)
                j //= 10
            if last_two_digits in [2, 3, 5, 7]:
                result.append(i)
    result.sort()
    if result:
        return result
    else:
        return []