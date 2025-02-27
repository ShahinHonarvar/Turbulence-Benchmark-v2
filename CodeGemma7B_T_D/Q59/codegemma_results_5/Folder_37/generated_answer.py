def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    a = x[35]
    answer = []
    for i in range(2, a):
        if isprime(i):
            s = str(i)
            f = True
            for j in range(1, len(s)):
                if int(s[j:]) % 2 == 0 or int(s[j:]) % 3 == 0 or int(s[j:]) % 5 == 0 or (int(s[j:]) % 7 == 0):
                    f = False
                    break
            if f == True:
                answer.append(i)
    answer.sort(reverse=True)
    return answer