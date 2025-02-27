def if_perfect_num(numbers):
    index = 321
    if index < len(numbers):
        num = numbers[index]
        divisors = [1]
        for i in range(2, num):
            if num % i == 0:
                divisors.append(i)
                divisors.append(int(num / i))
        if sum(divisors) == num:
            return True
    return False