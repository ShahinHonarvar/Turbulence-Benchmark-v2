def all_left_truncatable_prime(t: tuple) -> list:

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[100]
    result = [i for i in range(x, 1, -1) if is_prime(i)]

    def is_left_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) for i in range(len(str_n)))) and (not '0' in str_n)
    return [i for i in result if is_left_truncatable(i)][::-1]