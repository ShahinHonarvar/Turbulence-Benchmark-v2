def all_right_truncatable_prime(aTuple):
    x = aTuple[14]
    prime_list = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_prime = [i for i in prime_list if all((i % int(str(i)[:-k]) == 0 for k in range(1, len(str(i)))))]
    return sorted(right_truncatable_prime) if right_truncatable_prime else []