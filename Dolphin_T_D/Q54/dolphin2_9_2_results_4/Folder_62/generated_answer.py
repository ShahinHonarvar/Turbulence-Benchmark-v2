def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    x = t[70]
    prime_list = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list) if prime_list else []