def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[28]
    result = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp > 1:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                result.append(i)
    return sorted(result)