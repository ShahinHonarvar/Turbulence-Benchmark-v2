import math

def right_truncatable_prime(x):
    """
    Function to return all right truncatable primes less than x
    """
    primes = [2]
    for num in range(3, x):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            for i in range(0, int(math.log10(num)) + 1):
                digits = int(math.log10(num)) + 1 - i
                if num % math.pow(10, digits) / math.pow(10, digits - 1) in primes:
                    other_digits = int(num % math.pow(10, digits - 1) / math.pow(10, digits - 2))
                    if other_digits in primes:
                        continue
                    else:
                        break
            else:
                primes.append(num)
    return sorted([p for p in primes if p < x], reverse=True)