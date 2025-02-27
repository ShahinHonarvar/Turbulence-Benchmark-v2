def palindromes_of_specific_lengths(s):
    result = set()
    s = s[14:73].lower()
    for i in range(19, 56):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                result.add(s[j:j + i])
    return result