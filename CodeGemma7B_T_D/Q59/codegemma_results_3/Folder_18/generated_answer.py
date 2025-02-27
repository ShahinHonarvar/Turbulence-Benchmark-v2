def all_left_truncatable_prime(tup):
    x = tup[429]
    prime_list = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    prime_list = [i for i in prime_list if not any(str(i) == '0')]
    result = []
    for i in prime_list:
        if all((str(i)[-j:] in prime_list for j in range(1, len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)