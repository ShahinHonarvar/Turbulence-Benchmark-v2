def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[57]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            number = i
            while number > 1 and all([is_prime(int(str(number).replace(str(number)[-1], ''))) for _ in range(len(str(number))) if len(str(number)) > 1]):
                number = int(str(number).replace(str(number)[-1], '', 1))
                if len(str(number)) == 1:
                    result.append(i)
    return sorted(result, reverse=True)