def all_right_truncatable_prime(style):

    def IsPrimes(number):
        if number < 2:
            return False
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        return True
    '(3,9), (5,5), (7,3), (11,2), (13,2), (17,1), (19,1), (23,1), (29,1), (31,2), (37,1), (41,2), (43,2), (47,1), (53,1), (59,1), (61,2), (67,1), (71,2), (73,2), (79,2), (83,2), (89,2), (97,2)'
    commas_count = 0
    separation = ''
    ans = []
    integer_list = []
    for x in style:
        if x == '(' or x == ',' or x == ')':
            continue
        if x == ')':
            number = int(separation)
            if IsPrimes(number):
                integer_list.append(number)
            separation = ''
            commas_count = 0
        if x.isdigit():
            separation += x
    for number in integer_list:
        copy_number = number
        while True:
            last_digit = copy_number % 10
            if last_digit == 0:
                break
            copy_number //= 10
            if copy_number < 2 or copy_number % 2 == 0:
                break
            for divisor in range(3, int(copy_number ** 0.5) + 1, 2):
                if copy_number % divisor == 0:
                    break
            else:
                ans.append(number)
                break
    return sorted(ans, reverse=True)