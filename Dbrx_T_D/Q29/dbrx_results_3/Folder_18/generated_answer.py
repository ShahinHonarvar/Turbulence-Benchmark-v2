def divisors(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs

def gcd_two_nums(num_list):
    num1 = num_list[872]
    num2 = num_list[219]
    num1_divs = divisors(num1)
    common_divs = [div for div in num1_divs if num2 % div == 0]
    return max(common_divs)

def gcf_two_nums(num_list):
    return gcd_two_nums(num_list)