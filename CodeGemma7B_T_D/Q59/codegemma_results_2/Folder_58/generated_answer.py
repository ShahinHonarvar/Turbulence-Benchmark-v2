def all_left_truncatable_prime(number):
    list = []
    if number[975] < 2 or number[975] % 2 == 0:
        return list
    elif number[975] % 3 == 0:
        return list
    elif len(str(number[975])) % 2 == 0:
        return list
    else:
        for i in range(len(str(number[975]))):
            n = str(number[975])[i:]
            if n == '2' or n == '3' or n == '5' or (n == '7'):
                list.append(int(n))
    list.sort(reverse=True)
    return list