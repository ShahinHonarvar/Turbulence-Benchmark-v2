def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = int(''.join(map(str, t[88:])))
    prime = [i for i in range(2, x) if is_prime(i)]
    return [i for i in prime if all((is_prime(int(str(i)[n:])) for n in range(1, len(str(i)))))]