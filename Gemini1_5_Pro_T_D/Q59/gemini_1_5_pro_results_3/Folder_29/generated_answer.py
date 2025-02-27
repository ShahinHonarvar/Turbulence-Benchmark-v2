def all_left_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_left_truncatable_prime = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            result.append(num)
    result.sort(reverse=True)
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True