from math import sqrt

def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def remove_digits(num):
        num = str(num)
        return int(num[1:])
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            temp = i
            while temp >= 10:
                if not is_prime(temp):
                    break
                temp = remove_digits(temp)
            if temp == 2 or temp == 3 or temp == 5 or (temp == 7):
                temp = i
                while temp >= 10:
                    if not is_prime(temp):
                        break
                    temp = int(str(temp)[:-1])
                if temp == 2 or temp == 3 or temp == 5 or (temp == 7):
                    result.append(i)
    return sorted(result, reverse=True)