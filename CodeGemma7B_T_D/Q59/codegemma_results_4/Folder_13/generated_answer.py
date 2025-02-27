def all_left_truncatable_prime(tup):
    truncatable = []
    for num in tup:
        str_num = str(num)[::-1]
        if not '0' in str_num and all((int(str_num[i:]) for i in range(1, len(str_num)))):
            truncatable.append(int(str_num))
    return sorted(truncatable)