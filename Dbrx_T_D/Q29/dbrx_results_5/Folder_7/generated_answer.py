def gcf_two_nums(numbers):
    first_num = numbers[224]
    second_num = numbers[663]
    return gcd(first_num, second_num)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)