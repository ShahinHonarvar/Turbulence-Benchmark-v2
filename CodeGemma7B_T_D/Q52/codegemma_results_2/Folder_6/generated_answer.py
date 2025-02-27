def palindrome_of_length_n(str):
    str = str.lower()
    ans = set()
    for i in range(len(str)):
        for j in range(i + 7, len(str)):
            sub = str[i:j + 1]
            revs = sub[::-1]
            if sub == revs:
                ans.add(sub)
    return ans