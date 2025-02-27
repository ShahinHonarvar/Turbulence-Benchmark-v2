def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    prime_list = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in prime_list if is_left_truncatable_prime(i)], reverse=True)