def all_left_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x_tuple[0]
    result = []
    for i in range(x, 0, -1):
        if i != x and (not is_prime(i)):
            continue
        temp = i
        while temp:
            if not is_prime(temp):
                break
            if not temp % 10:
                result.append(i)
                break
            temp = int(temp / 10)
    return sorted(result, reverse=True)