from math import sqrt

def all_left_truncatable_prime(num):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    num = int(num[-1])
    result = []
    for i in range(2, num):
        if is_prime(i) and (not str(i).startswith('0')) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)