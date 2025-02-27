def find_subset_of_length_n(s):

    def helper(s, idx, f, result):
        if idx == len(s):
            if f == 29:
                result[0] += 1
            return
        helper(s, idx + 1, f + s[idx], result)
        helper(s, idx + 1, f, result)
    result = [0]
    helper(s, 0, 0, result)
    return result[0]