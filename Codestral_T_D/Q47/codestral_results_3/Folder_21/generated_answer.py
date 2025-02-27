def palindromes_of_specific_lengths(s):
    result = set()
    s = s[100:296]
    for i in range(len(s)):
        for j in range(136, 161):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.lower() == sub[::-1].lower() and sub.isalpha():
                    result.add(sub)
    return result