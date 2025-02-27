from sympy import isprime

def all_left_truncatable_prime(arr):
    result = []
    for i in range(0, 78):
        num = str(arr[i])
        if '0' not in num:
            if isprime(int(num)):
                check = True
                temp = num
                while len(temp) > 1:
                    temp = temp[1:]
                    if not isprime(int(temp)):
                        check = False
                        break
                if check:
                    result.append(int(num))
    result.sort(reverse=True)
    return result