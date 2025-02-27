def check_prime_number(num):
    if num == 2 or num == 3 or num == 2 ** num - 1:
        return True
    for i in range(5, num, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def get_all_truncatable(x):
    result = []
    for i in range(2, x):
        if check_prime_number(i):
            temp = str(i)
            for j in range(1, len(temp)):
                num = int(temp[:-j])
                if check_prime_number(num):
                    result.append(num)
                    break
    return sorted(result)