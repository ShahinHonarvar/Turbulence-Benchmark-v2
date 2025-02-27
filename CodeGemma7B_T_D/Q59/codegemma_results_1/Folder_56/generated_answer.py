def all_left_truncatable_prime(n):
    return_trunct = []
    for i in range(1, n):
        if 0 not in str(i):
            trunc = False
            num_str = str(i)
            for j in range(1, len(num_str)):
                if int(num_str[j:]) % 2 == 0 or int(num_str[j:]) % 3 == 0:
                    trunc = True
                    break
            if not trunc:
                return_trunct.append(i)
    return return_trunct