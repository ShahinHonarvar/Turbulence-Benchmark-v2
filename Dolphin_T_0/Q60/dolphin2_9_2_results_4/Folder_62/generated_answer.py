def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[70]
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i):
            left_right_truncatable = True
            for j in range(1, len(str(i)) - 1):
                if not is_prime(int(str(i)[j:len(str(i)) - j])):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(i)
    return primes