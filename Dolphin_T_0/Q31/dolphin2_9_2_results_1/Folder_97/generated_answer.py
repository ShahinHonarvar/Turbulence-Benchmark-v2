def if_perfect_num(L):
    if len(L) > 132:
        num = L[132]
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i == num // i:
                    sum += i
                else:
                    sum += i + num // i
        return sum == num
    return False