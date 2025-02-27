def all_right_truncatable_prime(t):
    x = t[70]
    prime_lst = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncatable_prime = True
            temp = i
            while temp > 0:
                digit = temp % 10
                temp //= 10
                if digit == 0 or (temp != 0 and (not is_prime(temp))):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                prime_lst.append(i)
    prime_lst.sort()
    return prime_lst

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True