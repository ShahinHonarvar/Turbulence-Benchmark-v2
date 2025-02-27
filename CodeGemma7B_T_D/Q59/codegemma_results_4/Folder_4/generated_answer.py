def all_left_truncatable_prime(x):
    for num in range(2, x):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0) or (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0) or (num % 19 == 0) or (num % 23 == 0) or (num % 29 == 0) or (num % 31 == 0) or (num % 37 == 0) or (num % 41 == 0) or (num % 43 == 0) or (num % 47 == 0) or (num % 53 == 0) or (num % 59 == 0) or (num % 61 == 0) or (num % 67 == 0) or (num % 71 == 0) or (num % 73 == 0) or (num % 79 == 0) or (num % 83 == 0) or (num % 89 == 0) or (num % 97 == 0):
            continue
        str_num = str(num)
        str_num = str_num[1:]
        while len(str_num) > 1:
            if str_num[0] == '0' or str_num[0] % 2 == 0 or str_num[0] % 3 == 0 or (str_num[0] % 5 == 0) or (str_num[0] % 7 == 0) or (str_num[0] % 11 == 0) or (str_num[0] % 13 == 0) or (str_num[0] % 17 == 0) or (str_num[0] % 19 == 0) or (str_num[0] % 23 == 0) or (str_num[0] % 29 == 0) or (str_num[0] % 31 == 0) or (str_num[0] % 37 == 0) or (str_num[0] % 41 == 0) or (str_num[0] % 43 == 0) or (str_num[0] % 47 == 0) or (str_num[0] % 53 == 0) or (str_num[0] % 59 == 0) or (str_num[0] % 61 == 0) or (str_num[0] % 67 == 0) or (str_num[0] % 71 == 0) or (str_num[0] % 73 == 0) or (str_num[0] % 79 == 0) or (str_num[0] % 83 == 0) or (str_num[0] % 89 == 0) or (str_num[0] % 97 == 0):
                break
            str_num = str(int(str_num))
            str_num = str_num[1:]
        if len(str_num) == 1:
            return [num]