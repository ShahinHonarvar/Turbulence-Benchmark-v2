def all_left_truncatable_prime(tpl):
    x = tpl[97]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:] + num_str[:i])):
                return False
        return True
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)