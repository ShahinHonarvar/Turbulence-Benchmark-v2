def all_left_truncatable_prime(t):

    def is_prime_without_0(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[23]
    left_truncatable_prime_list = []
    for y in range(1, x):
        if is_prime_without_0(y):
            temp = y
            while temp:
                temp = int(str(temp)[1:])
                if is_prime_without_0(temp):
                    continue
                else:
                    left_truncatable_prime_list.append(y)
                    break
    return sorted(list(set(left_truncatable_prime_list)))