def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x_tuple[98]
    result = []
    for i in range(10, x + 1):
        if '0' not in str(i):
            temp = i
            while len(str(temp)) > 2:
                temp = temp // 10
                if not is_prime(temp):
                    break
            else:
                result.append(i)
    return sorted(result)