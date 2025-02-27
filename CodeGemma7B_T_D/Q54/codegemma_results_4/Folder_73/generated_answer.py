def all_right_truncatable_prime(t):
    x = t[97]
    list = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            for k in range(1, len(str_i)):
                truncated_num = int(str_i[:-k])
                if truncated_num <= 1:
                    break
                is_truncated_prime = True
                for l in range(2, truncated_num):
                    if truncated_num % l == 0:
                        is_truncated_prime = False
                        break
                if is_truncated_prime:
                    list.append(i)
    list.sort()
    return list