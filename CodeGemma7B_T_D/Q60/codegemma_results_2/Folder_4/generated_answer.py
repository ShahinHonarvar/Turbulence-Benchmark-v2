def all_left_right_truncatable_prime(tup):
    prime_nums = [i for i in range(2, tup[96] + 1) if all((j not in str(i) for j in ('0', '5', '6', '8')))]
    result = []
    for i in range(len(prime_nums)):
        num = prime_nums[i]
        str_num = str(num)
        if len(str_num) == 1 or (len(str_num) == 2 and int(str_num) <= 3):
            continue
        flag = True
        if not str_num[0] == '2' and (not str_num[0] == '5'):
            for j in range(len(str_num) - 1):
                new_num = int(str_num[j + 1:])
                if not new_num in prime_nums or str(new_num)[-1] not in '37':
                    flag = False
                    break
        if flag:
            result.append(num)
    return sorted(result, reverse=True)