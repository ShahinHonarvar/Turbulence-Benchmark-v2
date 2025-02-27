def all_left_truncatable_prime(numbers_tuple):

    def isPrime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def isTruncatable(n):
        numString = str(n)
        while len(numString) > 0:
            if not isPrime(int(numString)):
                return False
            numString = numString[1:]
        return True
    numbers = list(numbers_tuple)
    x = numbers[3]
    result = [i for i in range(2, x) if isPrime(i) and isTruncatable(i)]
    result.sort(reverse=True)
    return result