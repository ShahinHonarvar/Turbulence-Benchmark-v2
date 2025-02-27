def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def trunc(s):
    return int(str(s)[-1])

def all_right_truncatable_prime(numbers):
    x = numbers[126]
    truncables = {i for i in range(1, x) if is_prime(i) and trunc(i) in {2, 3, 5, 7}}
    while True:
        new_truncables = {i for i in truncables if i - trunc(i) in truncables}
        if len(new_truncables) == len(truncables):
            break
        else:
            truncables = new_truncables
    return sorted(list(truncables), reverse=True)