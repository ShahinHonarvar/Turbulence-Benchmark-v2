def all_right_truncatable_prime(t):
    x = t[79]

    def is_prime(a):
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    def right_truncatable(a):
        if not is_prime(a):
            return False
        num_str = str(a)
        for i in range(1, len(num_str)):
            new_num = int(num_str[:-i])
            if not is_prime(new_num):
                return False
        return True
    result = [i for i in range(2, x) if right_truncatable(i)]
    return sorted(result, reverse=True) if result else []