from sympy import isprime

def all_left_right_truncatable_prime(in_tuple):
    x = in_tuple[70]
    x_list = []
    for number in range(2, x + 1):
        if isprime(number):
            str_num = str(number)
            if str_num.count('0') == 0:
                for index in range(1, len(str_num)):
                    if isprime(int(str_num[:index])) and isprime(int(str_num[index:])):
                        x_list.append(number)
    x_list.sort(reverse=True)
    return x_list