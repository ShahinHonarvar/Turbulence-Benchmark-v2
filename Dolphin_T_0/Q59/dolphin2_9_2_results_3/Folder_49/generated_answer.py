import math

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[14]
    output = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp > 1:
                if not is_prime(temp):
                    break
                temp //= 10
                if temp == 0:
                    output.append(i)
    return sorted(output)