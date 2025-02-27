from sympy import isprime

def all_left_right_truncatable_prime(num):

    def is_valid(digit):
        if digit == 0:
            return False
        return isprime(digit)

    def left_truncatable(left):
        list = []
        left = str(left)
        for i in range(1, len(left)):
            left = int(left[i:])
            if not is_valid(left):
                return False
            elif isprime(left):
                list.append(left)
        return list

    def right_truncatable(right):
        list = []
        right = str(right)
        for i in range(1, len(right)):
            right = int(right[:-i])
            if not is_valid(right):
                return False
            elif isprime(right):
                list.append(right)
        return list
    list = []
    for number in range(3, num + 1):
        left_list = left_truncatable(number)
        right_list = right_truncatable(number)
        if len(left_list) > 0 and len(right_list) > 0:
            for left in left_list:
                for right in right_list:
                    if left == right:
                        list.append(left)
    return sorted(list, reverse=True)