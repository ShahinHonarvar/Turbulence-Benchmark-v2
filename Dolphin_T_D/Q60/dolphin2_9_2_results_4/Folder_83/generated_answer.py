def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    result = []
    for num in range(x + 1):
        if is_prime(num) and '0' not in str(num):
            left_right_num = num
            while len(str(left_right_num)) >= 2:
                if is_prime(int(str(left_right_num)[1:-1])):
                    left_right_num = int(str(left_right_num)[1:-1])
                else:
                    break
            if left_right_num.isdigit() and is_prime(int(left_right_num)):
                result.append(num)
    return result