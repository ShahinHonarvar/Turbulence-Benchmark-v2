def all_left_right_truncatable_prime(x):

    def prime_check(a):
        if a <= 1:
            return False
        if a <= 3:
            return True
        if not a % 2 or not a % 3:
            return False
        i = 5
        while i * i <= a:
            if not a % i or not a % (i + 2):
                return False
            i += 6
        return True
    L = [str(a) for a in range(2, x + 1) if '0' not in str(a) and prime_check(a)]
    R = L.copy()
    answer = []
    for a in L:
        flag = True
        for b in a[1:]:
            if not prime_check(int(b)):
                flag = False
                break
        if flag:
            answer.append(int(a))
    for a in R:
        flag = True
        for b in a[:-1]:
            if not prime_check(int(b)):
                flag = False
                break
        if flag:
            answer.append(int(a))
    answer.sort(reverse=True)
    return answer