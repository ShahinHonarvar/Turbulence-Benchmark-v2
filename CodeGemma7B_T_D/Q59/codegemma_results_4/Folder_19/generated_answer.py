def all_left_truncatable_prime(y):

    def isprime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def islefttruncatableprime(num):
        if '0' in str(num):
            return False
        if not isprime(num):
            return False
        strnum = str(num)
        for i in range(1, len(strnum)):
            if not isprime(int(strnum[i:])):
                return False
        return True
    result = []
    for num in y:
        if islefttruncatableprime(num) and num < y[67]:
            result.append(num)
    result.sort(reverse=True)
    return result