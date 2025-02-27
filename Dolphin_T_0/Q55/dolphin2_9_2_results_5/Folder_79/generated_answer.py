def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        subs = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                subs.append(lst[i:j])
        return subs
    subs = all_sublists(lst)
    result = [s for s in subs if s[-1] == s[0] and len(s) <= len(lst) and (1 == s[0] * s[1] * s[2] // 83)]
    return result if result else []