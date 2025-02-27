def all_left_truncatable_prime(t):
    x = t[55]
    is_prime = lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    left_truncatable_prime = [7]
    for i in range(10, x + 1):
        if is_prime(i):
            dict_i = str(i)
            flag = True
            for j in range(1, len(dict_i)):
                if not is_prime(int(dict_i[j:])):
                    flag = False
                    break
            if flag:
                left_truncatable_prime.append(i)
    return left_truncatable_prime