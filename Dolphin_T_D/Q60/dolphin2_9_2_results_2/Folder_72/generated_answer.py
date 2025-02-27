import math

def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[31]
    ''.join(filter(lambda x: x.isdigit(), str(x)))
    prime_numbers = []
    for i in range(2, x):
        if str(i).isdigit() and is_prime(i):
            obj = i
            while obj != 1 and obj != 2:
                if not is_prime(obj):
                    break
                obj = int(str(obj)[1:-1])
            else:
                prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)