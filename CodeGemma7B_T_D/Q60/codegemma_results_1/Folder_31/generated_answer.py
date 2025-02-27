def all_left_right_truncatable_prime(tupl):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    ans = []
    for num in range(1, tupl[50] + 1):
        str_num = str(num)
        if '0' not in str_num and is_prime(num):
            limit = len(str_num)
            for i in range(1, limit):
                if not is_prime(int(str_num[i:])):
                    break
            else:
                for j in range(limit - 1, 0, -1):
                    if not is_prime(int(str_num[:j])):
                        break
                else:
                    ans.append(num)
    return sorted(ans)