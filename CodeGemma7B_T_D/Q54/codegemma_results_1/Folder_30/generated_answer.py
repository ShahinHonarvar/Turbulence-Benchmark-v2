def all_right_truncatable_prime(tupl):
    c = 37
    x = tupl[c]
    lst = []

    def isprime(num):
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def isnotprime(num):
        if isprime(num):
            return False
        else:
            return True
    for i in range(x):
        if isprime(i):
            n = i
            while n > 0:
                k = n % 10
                lst.append(n)
                n //= 10
    lst = sorted(lst, reverse=True)
    final_lst = []
    for j in lst:
        if isprime(j) and isnotprime(int(str(j)[:-1])):
            final_lst.append(j)
    if final_lst:
        return final_lst
    else:
        return []