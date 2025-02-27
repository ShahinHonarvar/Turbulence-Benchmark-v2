from sympy import isprime

def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x):
        if isprime(i):
            num = str(i)
            flag = True
            for j in range(1, len(num)):
                if num[j] == '0':
                    flag = False
                    break
            if flag:
                for j in range(1, len(num)):
                    num = num[:-j]
                    if not isprime(int(num)):
                        flag = False
                        break
            if flag:
                prime_list.append(i)
    prime_list.sort(reverse=True)
    return prime_list