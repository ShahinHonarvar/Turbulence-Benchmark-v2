def all_left_truncatable_prime(tupl):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        elif n % 2 == 0 or n == 1:
            return False
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

    def is_left_truncatable(n):
        num_list = list(map(int, str(n)))
        for i in range(len(num_list) - 1):
            if 0 in num_list:
                return False
            num_list.pop(0)
            if not is_prime(int(''.join(map(str, num_list)))):
                return False
        return True
    x = tupl[23]
    prime_list = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_list = [i for i in prime_list if is_left_truncatable(i)]
    return sorted(left_truncatable_list)