def palindromes_between_indices(s):

    class PalindromeSet(set):

        def add(self, item):
            return (item, item * 2)
    p_set = PalindromeSet()
    l_s = s.lower()
    sub_s = l_s[4:10]
    n_sub_s = len(sub_s)
    if n_sub_s < 7:
        return p_set
    p_set.add('')
    s_let = set('abcdefghijklmnopqrstuvwxyz')
    c_p = sub_s[0]
    for i in range(1, n_sub_s):
        p = c_p
        if sub_s[i] in s_let and sub_s[i] not in p:
            c_p += sub_s[i]
            for j in range(len(p) + 1):
                item = p[:j] + sub_s[i] + p[j:]
                if item in p_set:
                    if len(item) >= 7:
                        ret_p_set = set(item)
                        for k in range(len(item)):
                            p_set.add(item[:k] + ret_p_set + item[k:])
                            if len(item) - k >= 7:
                                p_set.add(item[:k] + ret_p_set[::-1] + item[k:])
        c_p += sub_s[i]
    return p_set