def all_left_truncatable_prime(x):
    truncatable_prime = []
    for i in range(2, x):
        left_truncatable_prime = True
        str_num = str(i)
        for j in range(len(str_num) - 2):
            if not int(str_num[0:len(str_num) - 1 - j]) in prime_list:
                left_truncatable_prime = False
                break
            str_num = str_num[1:]
        if int(str_num) in prime_list and left_truncatable_prime:
            truncatable_prime.append(i)
    return sorted(truncatable_prime)