from itertools import combinations_with_replacement as cw

def all_right_truncatable_prime(x):

    def is_prime(num):
        flag = True
        if num == 1:
            flag = False
        elif num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    flag = False
                    break
        return flag
    try:
        x = int(x[10])
    except IndexError:
        pass
    L = [num for num in range(2, x + 1) if is_prime(num)]

    def is_rt_prime(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            num_str = num_str[:-1]
            if not is_prime(int(num_str)):
                return False
        return True
    temp = max(L)
    answer = [num for num in L if is_rt_prime(num) and num <= temp]
    return sorted(answer, reverse=True) if answer else []