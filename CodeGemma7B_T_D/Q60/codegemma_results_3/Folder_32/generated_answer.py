def all_left_right_truncatable_prime(x):
    l, r = (3, 5 if x <= 8 else 3, 3 + (x - 8) // 6)
    prime_list = {i for i in range(l, r) if all((i % j for j in range(2, int(i ** 0.5) + 1)))}
    result = []
    for p in prime_list:
        if all((str(p)[i:len(str(p)) - i] in prime_list for i in range(1, len(str(p)) // 2 + 1))):
            result.append(p)
    return sorted(result) if result else []