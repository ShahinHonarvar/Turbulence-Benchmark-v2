def all_right_truncatable_prime(t):
    x = t[630]
    prime_set = {i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))}
    prime_list = list(prime_set)
    result = []
    for p in prime_list:
        chars = str(p)
        for i in range(1, len(chars)):
            new_p = int(chars[:-i])
            if new_p not in prime_set:
                break
        else:
            result.append(p)
    return sorted(result, reverse=True)