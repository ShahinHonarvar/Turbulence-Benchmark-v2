def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def all_left_truncatable_prime(ints):
    x = ints[18]
    primes_less_x = [i for i in range(x - 1, 1, -1) if is_prime(i)]
    left_truncatable_primes = [i for i in primes_less_x if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes