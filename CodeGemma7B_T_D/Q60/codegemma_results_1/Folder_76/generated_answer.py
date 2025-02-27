import math

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        return n > 1 and all((n % i for i in range(3, int(math.sqrt(n)) + 2, 2)))
    ans = []
    for i in range(2, x + 1):
        if not ('0' in str(i) or i % 2 == 0 or i % 3 == 0 or (i % 5 == 0)):
            y = str(i)
            l = len(y)
            if is_prime(i):
                for k in range(1, int(l / 2)):
                    if is_prime(int(y[k:])) or (int(y[k:]) % 2 == 0 or int(y[k:]) % 3 == 0 or int(y[k:]) % 5 == 0):
                        break
                    if is_prime(int(y[:l - k])) or (int(y[:l - k]) % 2 == 0 or int(y[:l - k]) % 3 == 0 or int(y[:l - k]) % 5 == 0):
                        continue
                    ans.append(i)
    if len(ans) == 0:
        return ans
    else:
        return sorted(ans, reverse=True)