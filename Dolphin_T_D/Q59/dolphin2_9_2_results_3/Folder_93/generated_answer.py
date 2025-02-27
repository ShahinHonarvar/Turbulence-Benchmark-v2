def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    prime_list = []
    for num in range(2, x):
        if is_prime(num) and (not '0' in str(num)):
            i = 0
            flag = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    flag = False
                    break
                temp //= 10
                i += 1
            if flag:
                prime_list.append(num)
    return sorted(prime_list)