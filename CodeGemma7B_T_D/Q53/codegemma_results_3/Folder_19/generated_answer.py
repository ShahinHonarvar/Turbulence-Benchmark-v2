def palindrome_of_length_at_least_n(str):

    def helper(str, l, r, res):
        if l > r:
            return
        if r - l + 1 >= 23 and str[l:r + 1] == str[r:l - 1:-1]:
            res.add(str[l:r + 1])
        helper(str, l + 1, r, res)
        helper(str, l, r - 1, res)
    res = set()
    helper(str.lower(), 0, len(str) - 1, res)
    return res