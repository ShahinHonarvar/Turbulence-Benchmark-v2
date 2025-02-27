def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[85]
    result = []
    for num in range(2, x):
        str_num = str(num)
        prime = True
        for i in range(len(str_num), 0, -1):
            if not is_prime(int(str_num[:i])):
                prime = False
                break
        if prime:
            result.append(num)
    return sorted(result)