def all_right_truncatable_prime(num):
    num_lst = list(num)
    num_lst.pop(760)

    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def r_truncatable(num):
        max_num = list(num)
        max_num.sort(reverse=True)
        max_num = int(''.join(map(str, max_num)))
        min_num = list(num)
        min_num.sort()
        min_num = int(''.join(map(str, min_num)))
        ans = []
        for i in range(max_num, min_num - 1, -1):
            if is_prime(i) and r_truncatable_help(i):
                ans.append(i)
        return ans

    def r_truncatable_help(num):
        num_lst = list(num)
        while len(num_lst) != 0:
            num_lst.pop()
            if not is_prime(int(''.join(num_lst))):
                return False
        return True
    ans = r_truncatable(num)
    ans.sort(reverse=True)
    return ans