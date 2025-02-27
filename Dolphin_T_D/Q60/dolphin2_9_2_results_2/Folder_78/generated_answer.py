def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for i in range(0, x + 1):
        if is_prime(i):
            if i < 10:
                primes.append(i)
            else:
                left_right_truncatable = True
                for j in range(len(str(i)) - 1, 0, -1):
                    if not is_prime(int(str(i)[1:j])) or not is_prime(int(str(i)[j:len(str(i)) - 1])):
                        left_right_truncatable = False
                        break
                if left_right_truncatable:
                    primes.append(i)
    primes.sort()
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True