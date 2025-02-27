def all_right_truncatable_prime(x):
    for num in range(2, x):
        if is_prime(num):
            truncatable(num)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def truncatable(num):
    temp = str(num)
    n = len(temp)
    for i in range(1, n):
        temp = temp[:-1]
        num2 = int(temp)
        if not is_prime(num2):
            break
    else:
        result.append(num)