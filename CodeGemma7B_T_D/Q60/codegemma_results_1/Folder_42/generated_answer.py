def all_left_right_truncatable_prime(t):
    x = t[64]
    prime_list = [i for i in range(2, x + 1) if all((j % i != 0 for j in range(2, int(i ** 0.5) + 1)))]
    result = []
    for i in prime_list:
        if not set(str(i)) & {'0'} and i in [2, 3, 5, 7] or (i % 10 != 3 and [str(i)[0], str(i)[-1]] in [('2', '3'), ('3', '7'), ('5', '3'), ('7', '2')]):
            if all((int(str(i)[:-j]) in prime_list or int(str(i)[j:]) in prime_list for j in range(1, len(str(i)) - 1))):
                result.append(i)
    return sorted(result, reverse=True) or []