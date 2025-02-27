def find_subset_of_length_n(s):

    def find_subset(s, n):
        if n == 0:
            return [[]]
        else:
            a = []
            for i in range(len(s)):
                b = find_subset(s[i + 1:], n - 1)
                for item in b:
                    a.append([s[i]] + item)
            return a
    return len(find_subset(s, 40))