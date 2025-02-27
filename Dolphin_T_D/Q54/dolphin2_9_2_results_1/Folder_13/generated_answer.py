def all_right_truncatable_prime(tt):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    list_ = [i for i in sorted(set(tt)) if i < tt[784] and i > 1 and is_prime(i)]
    for i in range(len(list_) - 1, 0, -1):
        j = list_[i]
        list_ = [x for x in list_ if str(x) != str(j)[:len(str(x))]]
    return list_