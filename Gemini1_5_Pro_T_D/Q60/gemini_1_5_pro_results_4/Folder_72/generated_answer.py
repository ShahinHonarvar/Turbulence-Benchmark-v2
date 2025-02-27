def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    result = []
    for num in range(2, x + 1):
        if all_left_right_truncatable_prime_helper(num):
            result.append(num)
    return sorted(result, descending=True)

def all_left_right_truncatable_prime_helper(num):
    if num < 10:
        if num in (2, 3, 5, 7):
            return True
        else:
            return False
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    return all_left_right_truncatable_prime_helper(int(str(num)[1:])) and all_left_right_truncatable_prime_helper(int(str(num)[:-1]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True