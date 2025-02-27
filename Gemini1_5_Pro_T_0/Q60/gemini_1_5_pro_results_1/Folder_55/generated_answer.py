def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for num in range(2, x + 1):
        if all_left_right_truncatable_prime_helper(num):
            result.append(num)
    result.sort(reverse=True)
    return result

def all_left_right_truncatable_prime_helper(num):
    if num < 10 and num in {2, 3, 5, 7}:
        return True
    if '0' in str(num) or not is_prime(num):
        return False
    return all_left_right_truncatable_prime_helper(int(str(num)[1:])) and all_left_right_truncatable_prime_helper(int(str(num)[:-1]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True