def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    result = []
    for num in range(2, x + 1):
        if all((i != '0' for i in str(num))) and is_left_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    if any((i in str(n) for i in ['0', '2', '4', '5', '6', '8'])):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True