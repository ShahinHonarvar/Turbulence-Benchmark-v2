from math import sqrt

def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    x = tup[49]
    for i in range(2, x + 1):
        if str(i)[-1] == '0' or str(i)[-1] == '2' or str(i)[-1] == '4' or (str(i)[-1] == '6') or (str(i)[-1] == '8') or (str(i)[-1] == '5') or (str(i)[-1] == 'a') or (str(i)[-1] == 'e') or (str(i)[-1] == 'c') or (str(i)[-1] == '9'):
            continue
        j = i
        s = str(j)
        while j >= 10 ** len(s) and is_prime(j):
            current = j
            divisible = True
            for k in range(len(s)):
                current //= 10
                if current % 2 == 0 or current % 5 == 0 or str(current)[-1] == '0' or (str(current)[-1] == '4') or (str(current)[-1] == '6') or (str(current)[-1] == '8'):
                    divisible = False
                    break
            if divisible:
                result.append(i)
            j -= 1
    return sorted(result)