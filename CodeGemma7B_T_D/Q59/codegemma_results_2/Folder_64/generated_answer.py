def all_left_truncatable_prime(tup):
    x = tup[4]

    def is_prime(num):
        return all((num % i for i in range(2, int(num ** 0.5) + 1))) and num > 1
    res = []
    for n in range(3, x):
        if not any((str(n)[-i] == '0' for i in range(1, len(str(n))))):
            if is_prime(n):
                copy = n
                while copy:
                    if not is_prime(copy):
                        break
                    copy //= 10
                else:
                    res.append(n)
    return sorted(res)