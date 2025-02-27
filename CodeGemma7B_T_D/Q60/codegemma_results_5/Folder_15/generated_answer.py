import math

def all_left_right_truncatable_prime(x):

    def isprime(x):
        for i in range(2, round(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if isprime(i) and str(i) not in '0' and isprime(int(str(i)[1:])) and isprime(int(str(i)[:-1])):
            result.append(i)
    result.sort(reverse=True)
    return result