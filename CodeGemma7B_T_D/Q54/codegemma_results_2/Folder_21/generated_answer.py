from math import sqrt

def all_right_truncatable_prime(t):
    x = t[175]

    def right_truncatable_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        for i in range(1, int(str(n)[:-1])):
            if int(str(n)[:-i]) % 2 == 0 or int(str(n)[:-i]) % 3 == 0 or int(str(n)[:-i]) % 5 == 0 or (int(str(n)[:-i]) % 7 == 0):
                break
            elif right_truncatable_prime(int(str(n)[:-i])):
                return True
        return True
    ans = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            ans.append(i)
    return sorted(ans)