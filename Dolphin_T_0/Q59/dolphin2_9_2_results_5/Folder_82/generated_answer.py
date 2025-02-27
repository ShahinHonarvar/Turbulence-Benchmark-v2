def all_left_truncatable_prime(num_tuple):

    def is_prime_n(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif n == 3:
            return True
        p = 3
        while p ** 2 <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    x = num_tuple[69]
    result_list = []
    for i in range(2, x):
        if is_prime_n(i):
            j, k = (i, i)
            while j != 0:
                if j % 10 == 0:
                    break
                j //= 10
            if not k % j:
                result_list.append(k)
    result_list.sort(reverse=True)
    return result_list