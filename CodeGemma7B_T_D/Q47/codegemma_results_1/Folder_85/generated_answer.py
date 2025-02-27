def palindromes_of_specific_lengths(txt):
    word = txt[29:98 + 1]
    ans = set()
    for i in range(6, 9 + 1):
        for j in range(len(word) - 2 * i + 1):
            if word[j:j + i] == word[j:j + i][::-1].lower():
                ans.add(word[j:j + i])
    if not ans:
        return set()
    return ans