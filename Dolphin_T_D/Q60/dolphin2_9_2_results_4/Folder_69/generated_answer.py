def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[760]
    truncatable_primes = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' not in str_num:
            str_num_len = len(str_num)
            if str_num_len >= 3:
                last_digit = int(str_num[-1])
                first_digit = int(str_num[0])
                if all((int(str_num[i:j]) % first_digit != 0 and int(str_num[i:j]) % last_digit != 0 for i in range(str_num_len - 1) for j in range(i + 2, str_num_len + 1))) and all((int(str_num[i:j]) != 1 for i in range(str_num_len) for j in range(i + 1, str_num_len))) and all((int(str_num[i:j]) % last_digit != 0 and int(str_num[i:j]) % first_digit != 0 for i in range(str_num_len - 1) for j in range(i + 2, str_num_len + 1))) and all((int(str_num[i:j]) % first_digit != 0 and int(str_num[i:j]) % last_digit != 0 for i in range(str_num_len) for j in range(i + 1, str_num_len))):
                    truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)