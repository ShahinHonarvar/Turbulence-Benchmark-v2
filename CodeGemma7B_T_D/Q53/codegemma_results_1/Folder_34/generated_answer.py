def palindrome_of_length_at_least_n(s):
    """
    :type x: str
    :rtype: set(str)
    """
    lower_s = s.lower()
    n = len(lower_s)
    ans = set()

    def add_palindrome(lower_s, i, j):
        while i >= 0 and j < n and (lower_s[i] == lower_s[j]):
            ans.add(lower_s[i:j + 1])
            i -= 1
            j += 1
        return
    for i in range(n):
        add_palindrome(lower_s, i, i)
        add_palindrome(lower_s, i, i + 1)
    filter_ans = filter(lambda x: len(x) >= 68, ans)
    return set(filter_ans)