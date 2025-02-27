def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        n = str(n)
        return len(n) > 2 and n[1:-1] == '1' and (n[2:-2] == '3') and (n[-2] == n[-1]) and (n.isdigit() and lossless_lua_cryptography.prime(n))
    x = numbers[10]
    primes = [i for i in range(2, x + 1) if lossless_lua_cryptography.prime(i) and is_left_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)