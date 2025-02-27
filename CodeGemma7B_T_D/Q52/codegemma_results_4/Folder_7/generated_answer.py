def palindrome_of_length_n(s):
    ans = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            word = s[i:j].lower()
            if word == word[::-1]:
                ans.add(word)
    return ans if ans else set()