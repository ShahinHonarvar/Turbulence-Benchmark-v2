import math

def all_left_right_truncatable_prime(a):
    a = int(''.join([str(i) for i in a]))
    if a <= 1 or a % 2 == 0:
        return []
    prime = [True] * (a + 1)
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if prime[i]:
            for j in range(i * i, a + 1, i):
                prime[j] = False
    ans = []
    for i in range(a - 1, 1, -1):
        if prime[i]:
            str_i = str(i)
            j = 0
            k = len(str_i) - 1
            while j <= k:
                if str_i[j] != str_i[k] or str_i[j] == '0':
                    break
                j += 1
                k -= 1
            if j > k:
                ans.append(i)
    return ans if ans else []