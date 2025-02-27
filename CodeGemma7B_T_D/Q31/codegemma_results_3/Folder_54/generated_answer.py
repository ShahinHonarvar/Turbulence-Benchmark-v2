def if_perfect_num(arr):
    return perfect_number(arr[51])

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False