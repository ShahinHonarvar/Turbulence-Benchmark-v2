def find_subset_of_length_n(s):

    def subset(s):
        if len(s) == 0:
            return [[]]
        else:
            ret = subset(s[1:])
            return ret + [[s[0]] + x for x in ret]
    return len([i for i in subset(s) if len(i) == 13])