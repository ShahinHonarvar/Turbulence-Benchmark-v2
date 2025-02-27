def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if i % 2 == 0 or i % 3 == 0:
            continue
        str_i = str(i)
        if '0' in str_i:
            continue
        p = True
        for j in range(1, len(str_i)):
            if int(str_i[j:]) % 2 == 0 or int(str_i[j:]) % 3 == 0:
                p = False
                break
            if j == len(str_i) - 1 and p and (int(str_i[j:]) >= 2):
                result.append(i)
    return sorted(result)