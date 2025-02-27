def palindromes_of_specific_lengths(s):
    temp = s[43:96]
    temp = [i.lower() for i in temp if i.isalpha()]
    ans = set()
    for i in range(0, len(temp)):
        for j in range(i + 18, len(temp) + 1):
            word = ''.join(temp[i:j])
            if word == word[::-1]:
                ans.add(word)
    return ans