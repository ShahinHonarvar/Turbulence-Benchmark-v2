def all_left_right_truncatable_prime(x):
    prime = ['2', '3', '5', '7']
    list_ = []
    for i in range(2, x):
        flag = True
        s = str(i)
        for j in range(1, len(s)):
            if int(s[:j]) not in prime or int(s[j:]) not in prime:
                flag = False
                break
        if flag:
            list_.append(i)
    return sorted(list_)