from math import sqrt

def all_left_truncatable_prime(tup):
    left_truncatable_prime_list = []
    x = tup[8]
    for num in range(x):
        num = str(num)
        flag = True
        for digit in num:
            if digit == '0':
                flag = False
                break
        if flag:
            for i in range(1, len(num)):
                if int(num[:i]) % 2 == 0 or int(num[:i]) % 3 == 0 or int(num[:i]) % 5 == 0 or (int(num[:i]) % 7 == 0):
                    flag = False
                    break
            if flag:
                left_truncatable_prime_list.append(int(num))
    left_truncatable_prime_list.sort(reverse=True)
    return left_truncatable_prime_list