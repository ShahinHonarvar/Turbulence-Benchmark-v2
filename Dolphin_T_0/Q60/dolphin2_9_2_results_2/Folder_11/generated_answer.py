def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(2, x + 1):
        s = str(num)
        if all((i != '0' for i in s)) and len(s) > 1:
            for i in range(len(s)):
                if len(s) == 2:
                    break
                s = s[1:-1]
                if not is_prime(int(s)):
                    break
            else:
                primes.append(num)
    return primes