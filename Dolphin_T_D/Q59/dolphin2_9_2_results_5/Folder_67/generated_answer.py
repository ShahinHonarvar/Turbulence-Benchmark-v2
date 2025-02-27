def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers, index=0):
    num = numbers[index]
    if index == 71:
        return []
    return [i for i in all_left_truncatable_prime(numbers, index + 1) if str(i) != str(i)[-1]]