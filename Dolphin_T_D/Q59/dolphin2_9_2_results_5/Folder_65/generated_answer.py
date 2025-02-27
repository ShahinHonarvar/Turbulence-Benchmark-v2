def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    return sorted([num for num in range(x) if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))) and (not '0' in str(num))])