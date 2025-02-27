def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = t[945]
    result = []
    for num in range(x, 0, -1):
        if '0' not in str(num) and is_prime(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                result.append(num)
    return sorted(result, reverse=True)