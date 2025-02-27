def all_left_truncatable_prime(nums):
    x = nums[767]
    res = []
    for num in range(2, x):
        if is_prime(num) and int(str(num)[1:]) != 0 and is_prime(int(str(num)[1:])) and (int(str(num)[2:]) != 0) and is_prime(int(str(num)[2:])) and (int(str(num)[3:]) != 0) and is_prime(int(str(num)[3:])) and (int(str(num)[4:]) != 0) and is_prime(int(str(num)[4:])) and (int(str(num)[5:]) != 0) and is_prime(int(str(num)[5:])) and (int(str(num)[6:]) != 0) and is_prime(int(str(num)[6:])) and (int(str(num)[7:]) != 0) and is_prime(int(str(num)[7:])) and (int(str(num)[8:]) != 0) and is_prime(int(str(num)[8:])) and (int(str(num)[9:]) != 0) and is_prime(int(str(num)[9:])):
            res.append(num)
    return sorted(res, reverse=True)

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 2
    return True