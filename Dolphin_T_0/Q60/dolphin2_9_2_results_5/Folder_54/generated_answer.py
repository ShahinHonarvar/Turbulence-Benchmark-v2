def all_left_right_truncatable_prime(t):
    x = t[88]
    prime_numbers = [2, 3, 5, 7]
    for i in range(10, x):
        if is_prime(i):
            if i % 10 != 0:
                temp = i
                while temp >= 10:
                    temp = temp // 10
                    if int(str(temp)[0]) == 0 or not is_prime(temp):
                        break
                else:
                    temp = int(str(i)[::-1])
                    while temp >= 10:
                        temp = temp // 10
                        if int(str(temp)[-1]) == 0 or not is_prime(temp):
                            break
                    else:
                        prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True