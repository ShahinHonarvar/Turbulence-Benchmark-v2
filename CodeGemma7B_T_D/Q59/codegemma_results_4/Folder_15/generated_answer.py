def all_left_truncatable_prime(InputTuple):
    x = InputTuple[6]
    LeftTruncatablePrimes = []
    for i in range(2, x):
        if str(i).count('0') == 0 and is_prime(i):
            TruncatedNumber = str(i)
            while len(TruncatedNumber) > 1:
                TruncatedNumber = TruncatedNumber[1:]
                if not is_prime(int(TruncatedNumber)):
                    break
            else:
                LeftTruncatablePrimes.append(i)
    LeftTruncatablePrimes.sort(reverse=True)
    return LeftTruncatablePrimes

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True