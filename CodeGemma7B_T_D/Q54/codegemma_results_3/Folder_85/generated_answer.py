def all_right_truncatable_prime(x):
    result = []
    for i, num in enumerate(x):
        if i == 94:
            break
        test = all((i % j != 0 for j in range(2, num // 2 + 1)))
        if test:
            num_str = str(num)
            for j in range(1, len(num_str)):
                test = True
                for k in range(2, int(num_str[:len(num_str) - j]) // 2 + 1):
                    if int(num_str[:len(num_str) - j]) % k == 0:
                        test = False
                        break
                if test:
                    result.append(int(num_str[:len(num_str) - j]))
    return sorted(result)