def find_subset_of_length_n(s):

    def subset(s):
        if len(s) == 1:
            return [s, []]
        else:
            t = subset(s.pop())
            u = [s.pop()]
            return t + [[x] + u for x in t] + [u]
    l = subset(s)
    c = 0
    for i in l:
        if len(i) == 49:
            c = c + 1
    return c