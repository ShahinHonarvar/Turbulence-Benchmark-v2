def all_left_truncatable_prime(args):
    x = args[37]
    prime_list = ['2', '3']
    for i in range(3, x + 1):
        if i < 10:
            prime_list.append(str(i))
        else:
            start = 0
            while start < len(str(i)) and str(i)[start] != '0':
                start += 1
            if start != len(str(i)):
                continue
            cur = i
            while cur > 0:
                if not all((str(cur)[j:] in prime_list for j in range(len(str(cur))))):
                    break
                cur = cur // 10
            else:
                if cur == 1:
                    prime_list.append(str(i))
    prime_list.sort(reverse=True)
    return prime_list