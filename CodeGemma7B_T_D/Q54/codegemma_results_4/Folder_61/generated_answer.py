def all_right_truncatable_prime(tup):
    x = tup[3]
    nums = set(range(2, x))
    prime = set()
    for i in nums:
        flag = True
        temp = str(i)
        for j in range(1, len(temp)):
            temp = temp[:-j]
            if int(temp) in nums and int(temp) not in prime:
                flag = False
                break
        if flag:
            prime.add(i)
    return sorted(prime, reverse=True)