def all_right_truncatable_prime(args):
    x = args[11]
    results = []
    for num in range(2, x):
        is_prime = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if int(str_num[i:]) in [0, 2, 4, 6, 8]:
                is_prime = False
                break
            if int(str_num[i:]) % 3 == 0:
                is_prime = False
                break
            if int(str_num[i:]) % 5 == 0:
                is_prime = False
                break
        if is_prime:
            str_num = str(num)
            for i in range(1, len(str_num)):
                if int(str_num[:-i]) in [0, 2, 4, 6, 8]:
                    is_prime = False
                    break
                if int(str_num[:-i]) % 3 == 0:
                    is_prime = False
                    break
                if int(str_num[:-i]) % 5 == 0:
                    is_prime = False
                    break
            if is_prime:
                results.append(num)
    results.sort()
    return results if results else []