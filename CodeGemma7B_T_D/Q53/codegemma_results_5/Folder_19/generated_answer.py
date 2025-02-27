def palindrome_of_length_at_least_n(str):
    """
    :type str: str
    :rtype: set[str]
    """

    def helper(str, ans, idx, n):
        if idx == len(str):
            if len(ans) >= n:
                ans.add(ans)
            return
        elif len(ans) >= n:
            return
        else:
            for i in range(idx, len(str)):
                ans.append(str[i])
                helper(str, ans, i + 1, n)
                ans.pop()
    ans = set()
    helper(str, [], 0, 23)
    return ans