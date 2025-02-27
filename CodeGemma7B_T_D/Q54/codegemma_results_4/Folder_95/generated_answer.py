from functools import reduce

def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def num_list(n):
    return [int(d) for d in str(n)]

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    new_nums = []
    for i in range(2, x):
        digits = num_list(i)
        size = len(digits) - 1
        found = True
        for j in range(size):
            temp = digits[:size - j]
            k = reduce(lambda a, b: a * 10 + b, temp)
            if prime(k) == False:
                found = False
                break
        if found and prime(i):
            new_nums.append(i)
    return sorted(new_nums)