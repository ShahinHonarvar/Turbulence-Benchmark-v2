def find_subset_of_length_n(S):

    def find_subset(S, n):
        if n == 0:
            return [[]]
        elif n == 1:
            return [[i] for i in S]
        else:
            return [[i] + subset for i in S for subset in find_subset(S.difference({i}), n - 1)]
    return len(find_subset(S, 47))