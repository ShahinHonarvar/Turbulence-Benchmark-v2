def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    result = []
    for num in range(2, x + 1):
        if all((str(num)[i:] in '2357' and int(str(num)[i:]) > 1 and all((int(str(num)[i:]) % j for j in range(2, int(int(str(num)[i:]) ** 0.5) + 1))) and all((str(num)[:i] in '2357' and int(str(num)[:i]) > 1 and all((int(str(num)[:i]) % j for j in range(2, int(int(str(num)[:i]) ** 0.5) + 1))) for i in range(len(str(num))))) for i in range(len(str(num))))):
            result.append(num)
    return sorted(result)