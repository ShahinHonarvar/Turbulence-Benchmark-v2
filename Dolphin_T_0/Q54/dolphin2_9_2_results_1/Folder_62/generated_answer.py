def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        else:
            for key in range(2, int(n ** 0.5) + 1):
                if n % key == 0:
                    return False
            return True

    def is_rt_prime(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[:i])):
                return False
        return True
    x = input_tuple[70]
    ratio_primes = [int(n) for n in str(x)]
    result = [i for i in ratio_primes if is_rt_prime(i)]
    return sorted(result)