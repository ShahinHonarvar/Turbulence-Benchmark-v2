def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[100]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            for i in range(1, len(str_num)):
                left_trunk = str_num[i:]
                right_trunk = str_num[:-i]
                if left_trunk[0] == '0':
                    left_trunk = left_trunk[1:]
                if right_trunk[-1] == '0':
                    right_trunk = right_trunk[:-1]
                if all([int(left_trunk), int(right_trunk)]) and str(num).count(left_trunk) == 1 and (str(num).count(right_trunk) == 1):
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)